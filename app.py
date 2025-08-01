import streamlit as st
import io
import time # For exponential backoff
import json # For parsing Gemini API response
import requests # For making HTTP requests to Gemini API
import time # For exponential backoff (though less critical with external API)
import json # For parsing JSON responses
import requests # For making HTTP requests

# --- Page Configuration ---
st.set_page_config(
@@ -162,41 +162,24 @@
        {"role": "assistant", "content": "Hello! I'm Dr. X, your AI growth mindset coach. How can I help you explore your potential today?"}
    ]

# Function to call Gemini API with exponential backoff for chat
def get_gemini_chat_response_with_retry(chat_history_for_gemini, system_instruction, max_retries=5, initial_delay=1.0):
    # Prepend the system instruction to the chat history for this specific call
    full_chat_history = [{"role": "user", "parts": [{"text": system_instruction}]}]
    full_chat_history.append({"role": "model", "parts": [{"text": "Understood. I'm ready to help!"}]}) # Acknowledge system instruction
    for msg in chat_history_for_gemini:
        role = "user" if msg["role"] == "user" else "model"
        full_chat_history.append({"role": role, "parts": [{"text": msg["content"]}]})

    payload = {
        "contents": full_chat_history,
        "generationConfig": {
            "responseMimeType": "text/plain"
        }
    }
    api_key = "" # Canvas will provide this at runtime
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key={api_key}"

    for i in range(max_retries):
        try:
            response = requests.post(api_url, headers={'Content-Type': 'application/json'}, json=payload)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            result = response.json()

            if result.get("candidates") and result["candidates"][0].get("content") and result["candidates"][0]["content"].get("parts"):
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return "Error: Could not get feedback. Unexpected API response."
        except requests.exceptions.RequestException as e:
            if i < max_retries - 1:
                delay = initial_delay * (2 ** i)
                time.sleep(delay)
            else:
                return f"Error: Could not get feedback after {max_retries} retries: {e}"
    return "Error: Could not get feedback."
# Dr. X API function (from Quarterback Crown)
def ask_drx(message):
    try:
        response = requests.post(
            'https://ask-drx-730124987572.us-central1.run.app',
            json={'message': message},
            timeout=30
        )
        if response.status_code == 200:
            return response.json().get('reply', "Sorry, I couldn't process that.")
        else:
            return f"I'm having trouble connecting right now. Server responded with status {response.status_code}. Please try again."
    except requests.exceptions.Timeout:
        return "I'm having trouble connecting right now. The request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return "I'm having trouble connecting right now. There was a network error. Please check your internet connection and try again."
    except Exception as e:
        return f"I'm having trouble connecting right now. An unexpected error occurred: {e}. Please try again."

# --- Dr. X General Chat Interface ---
st.header("💬 Talk to Dr. X (General Chat)")
@@ -214,11 +197,18 @@ def get_gemini_chat_response_with_retry(chat_history_for_gemini, system_instruct
    # Add user message to chat history
    st.session_state.general_chat_history.append({"role": "user", "content": prompt})

    system_instruction_general = "You are Dr. X, a friendly, encouraging, and knowledgeable AI growth mindset coach for middle and high school students. Your goal is to provide supportive, actionable advice on embracing challenges, learning from mistakes, and fostering a growth mindset. Keep responses concise and inspiring. Always maintain a positive and supportive tone."

    # Get assistant response
    # For the general chat, we can combine the history for a more conversational flow
    # Note: The external API might not maintain full conversational context on its own.
    # We'll send the latest prompt and rely on the external API's internal logic.
    # If the external API truly supports chat history, we'd send the full st.session_state.general_chat_history.
    # For now, we'll send the last user message as the 'message' to the external API.
    # A more robust solution would involve the external API managing session history.
    
    with st.spinner("Dr. X is thinking..."):
        assistant_response = get_gemini_chat_response_with_retry(st.session_state.general_chat_history, system_instruction_general)
        # Send only the latest user prompt to the external API for simplicity,
        # assuming the external API handles its own context or is designed for single-turn questions.
        # If the external API supports full chat history, you would pass a more complex structure here.
        assistant_response = ask_drx(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
@@ -233,62 +223,62 @@ def get_gemini_chat_response_with_retry(chat_history_for_gemini, system_instruct

# Challenge Entry
challenge_text = st.text_area("Describe a challenge you're facing:", height=100, key="journal_challenge_text")
if st.button("Get Feedback on Challenge", key="feedback_challenge_btn"): # Removed class_name
if st.button("Get Feedback on Challenge", key="feedback_challenge_btn"):
    if challenge_text:
        system_instruction_challenge = "You are Dr. X, a friendly growth mindset coach. Provide encouraging and constructive feedback specifically on the student's described challenge. Emphasize perseverance and learning."
        journal_prompt = f"As a growth mindset coach, provide encouraging and constructive feedback on this challenge: {challenge_text}. Emphasize perseverance and learning."
        with st.spinner("Dr. X is thinking..."):
            feedback = get_gemini_chat_response_with_retry([{"role": "user", "content": challenge_text}], system_instruction_challenge)
            feedback = ask_drx(journal_prompt)
            st.markdown(f"<div class='highlight-box'><p style='font-weight: bold; color: #388E3C;'>Dr. X's Feedback on your Challenge:</p><p style='color: #4CAF50;'>{feedback}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Please describe your challenge before getting feedback.")

# Effort Entry
effort_taken = st.text_area("What effort have you made so far?", height=100, key="journal_effort_taken")
if st.button("Get Feedback on Effort", key="feedback_effort_btn"): # Removed class_name
if st.button("Get Feedback on Effort", key="feedback_effort_btn"):
    if effort_taken:
        system_instruction_effort = "You are Dr. X, a friendly growth mindset coach. Acknowledge and praise the student's effort. Reinforce that effort is key to growth and encourage continued dedication."
        journal_prompt = f"As a growth mindset coach, acknowledge and praise the effort described: {effort_taken}. Reinforce that effort is key to growth and encourage continued dedication."
        with st.spinner("Dr. X is thinking..."):
            feedback = get_gemini_chat_response_with_retry([{"role": "user", "content": effort_taken}], system_instruction_effort)
            feedback = ask_drx(journal_prompt)
            st.markdown(f"<div class='highlight-box'><p style='font-weight: bold; color: #388E3C;'>Dr. X's Feedback on your Effort:</p><p style='color: #4CAF50;'>{feedback}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Please describe your effort before getting feedback.")

# Mistake Entry
mistake_text = st.text_area("Describe a mistake you’ve made:", height=100, key="journal_mistake_text")
if st.button("Get Feedback on Mistake", key="feedback_mistake_btn"): # Removed class_name
if st.button("Get Feedback on Mistake", key="feedback_mistake_btn"):
    if mistake_text:
        system_instruction_mistake = "You are Dr. X, a friendly growth mindset coach. Help the student reframe their mistake as a learning opportunity. Emphasize that mistakes are valuable for growth."
        journal_prompt = f"As a growth mindset coach, help reframe this mistake: {mistake_text}. Emphasize that mistakes are valuable for growth and learning."
        with st.spinner("Dr. X is thinking..."):
            feedback = get_gemini_chat_response_with_retry([{"role": "user", "content": mistake_text}], system_instruction_mistake)
            feedback = ask_drx(journal_prompt)
            st.markdown(f"<div class='highlight-box'><p style='font-weight: bold; color: #388E3C;'>Dr. X's Feedback on your Mistake:</p><p style='color: #4CAF50;'>{feedback}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Please describe your mistake before getting feedback.")

# Lesson Learned Entry
lesson_learned = st.text_area("What did you learn from that mistake?", height=100, key="journal_lesson_learned")
if st.button("Get Feedback on Lesson Learned", key="feedback_lesson_btn"): # Removed class_name
if st.button("Get Feedback on Lesson Learned", key="feedback_lesson_btn"):
    if lesson_learned:
        system_instruction_lesson = "You are Dr. X, a friendly growth mindset coach. Validate the student's learning from their mistake. Encourage them to apply this lesson in the future."
        journal_prompt = f"As a growth mindset coach, validate the learning from this mistake: {lesson_learned}. Encourage the student to apply this lesson in the future."
        with st.spinner("Dr. X is thinking..."):
            feedback = get_gemini_chat_response_with_retry([{"role": "user", "content": lesson_learned}], system_instruction_lesson)
            feedback = ask_drx(journal_prompt)
            st.markdown(f"<div class='highlight-box'><p style='font-weight: bold; color: #388E3C;'>Dr. X's Feedback on your Lesson Learned:</p><p style='color: #4CAF50;'>{feedback}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Please describe your lesson learned before getting feedback.")

# Growth Action Entry
growth_action = st.text_input("One action you’ll take to grow this week:", "e.g., Ask for help on a tough math problem", key="journal_growth_action")
if st.button("Get Feedback on Growth Action", key="feedback_growth_action_btn"): # Removed class_name
if st.button("Get Feedback on Growth Action", key="feedback_growth_action_btn"):
    if growth_action:
        system_instruction_action = "You are Dr. X, a friendly growth mindset coach. Provide encouraging feedback on the student's planned growth action. Emphasize the importance of taking concrete steps."
        journal_prompt = f"As a growth mindset coach, provide encouraging feedback on this planned growth action: {growth_action}. Emphasize the importance of taking concrete steps."
        with st.spinner("Dr. X is thinking..."):
            feedback = get_gemini_chat_response_with_retry([{"role": "user", "content": growth_action}], system_instruction_action)
            feedback = ask_drx(journal_prompt)
            st.markdown(f"<div class='highlight-box'><p style='font-weight: bold; color: #388E3C;'>Dr. X's Feedback on your Growth Action:</p><p style='color: #4CAF50;'>{feedback}</p></div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a growth action before getting feedback.")


# --- Export Button ---
if st.button("📅 Download My Journal as Text File", key="download_journal_btn"): # Removed class_name
if st.button("📅 Download My Journal as Text File", key="download_journal_btn"):
    buffer = io.StringIO()
    buffer.write("Growth Mindset Reflection Journal\n\n")
    buffer.write(f"Challenge: {challenge_text}\n")
