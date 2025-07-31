import streamlit as st
import io
import time # For exponential backoff
import json # For parsing Gemini API response
import requests # For making HTTP requests to Gemini API

# --- Page Configuration ---
st.set_page_config(
    page_title="CognitiveCloud.ai: Growth Mindset Explorer",
    page_icon="🌱", # A plant icon to symbolize growth
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for consistent styling (Inter font, CognitiveCloud.ai colors) ---
st.markdown("""
<style>
    body {
        font-family: 'Inter', sans-serif;
        background-color: #F8F7F4; /* Light neutral background */
        color: #333333; /* Dark text for readability */
    }
    .main-header {
        text-align: center;
        color: #6A0572; /* CognitiveCloud.ai primary header color */
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #4B0082; /* CognitiveCloud.ai secondary header color */
        font-size: 1.8rem;
        margin-bottom: 2rem;
    }
    .section-header {
        color: #005A9C; /* CognitiveCloud.ai accent blue */
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #E0E0E0;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 1px solid #E0E0E0;
    }
    .highlight-box {
        background-color: #E8F5E9; /* Light green for positive reinforcement */
        border-left: 5px solid #4CAF50; /* Green accent */
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .button-style {
        background-color: #005A9C; /* Accent blue button */
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        transition: background-color 0.3s ease;
        cursor: pointer;
        border: none;
    }
    .button-style:hover {
        background-color: #004070; /* Darker blue on hover */
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<h1 class="main-header">🌱 CognitiveCloud.ai: Growth Mindset Explorer</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unlock Your Potential: Embrace Challenges, Learn from Mistakes, and Grow!</p>', unsafe_allow_html=True)

# --- Welcome Card with Quotes ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Welcome, Future Achiever!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem;'>Your abilities grow with effort, mistakes, and perseverance. Let these voices guide your journey:</p>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The power of 'not yet'!" - Carol Dweck
    </p>
    <p style='color: #4CAF50;'>
        Instead of saying "I can't do it," try "I can't do it *yet*!" This simple shift opens up possibilities for learning and improvement.
    </p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "Success is not to be measured by where you stand in life, but by the obstacles you have overcome." - Booker T. Washington
    </p>
    <p style='color: #4CAF50;'>
        This powerful quote reminds us that true achievement comes from facing and conquering difficulties, not just from natural talent. Every challenge you overcome builds your capacity for future success.
    </p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The tragedy of life is not that it ends so soon, but that we wait so long to begin it." - Benjamin Elijah Mays
    </p>
    <p style='color: #4CAF50;'>
        Dr. Mays' words encourage us to seize the moment, embrace learning, and start pursuing our potential now, without hesitation or fear of failure. Every day is an opportunity to grow!
    </p>
</div>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "Invest in the human soul. Who knows, it might be a diamond in the rough." - Mary McLeod Bethune
    </p>
    <p style='color: #4CAF50;'>
        Mary McLeod Bethune's inspiring words highlight the immense, often hidden, potential within each individual, encouraging us to nurture and believe in our own and others' capacity for greatness.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Common Core Connections Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Connections to Common Core Standards</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    A growth mindset is a powerful tool that supports learning across all subjects and grade levels.
    While not a specific content standard, fostering a growth mindset directly impacts students' ability to meet and exceed Common Core State Standards (CCSS) in various disciplines.
</p>
<ul class="list-disc list-inside text-gray-700 space-y-2 mb-4">
    <li>**Mathematics (CCSS.Math.Practice.MP1-8):** The Standards for Mathematical Practice emphasize problem-solving, perseverance, reasoning, and precision. A growth mindset directly cultivates these practices by encouraging students to:
        <ul>
            <li>**Make sense of problems and persevere in solving them (MP1):** Students with a growth mindset view challenging problems as opportunities to learn, rather than obstacles.</li>
            <li>**Reason abstractly and quantitatively (MP2):** They are more willing to try different approaches and learn from mistakes when reasoning.</li>
            <li>**Attend to precision (MP6):** They see errors as feedback to improve their accuracy and understanding.</li>
        </ul>
    </li>
    <li>**English Language Arts (CCSS.ELA-Literacy.R.CCR.1-10, W.CCR.1-10):** A growth mindset helps students in ELA by:
        <ul>
            <li>**Reading closely and making logical inferences (R.CCR.1):** They are more open to re-reading and re-evaluating texts when faced with comprehension challenges.</li>
            <li>**Producing clear and coherent writing (W.CCR.4):** They embrace the iterative process of drafting, revising, and editing, seeing it as a path to better writing.</li>
        </ul>
    </li>
    <li>**Science & Engineering Practices (NGSS):** Similar to math, a growth mindset is essential for scientific inquiry and engineering design, encouraging students to:
        <ul>
            <li>**Ask questions and define problems (SEP1):** They are curious and not afraid to explore unknowns.</li>
            <li>**Construct explanations and design solutions (SEP6):** They persist through failures and iterate on their designs.</li>
        </ul>
    </li>
</ul>
<p style='font-size: 1.1rem; line-height: 1.6;'>
    By developing a growth mindset, students build the resilience and intellectual curiosity needed to master academic content and thrive in a rapidly changing world.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# Initialize session state for Dr. X chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Hello! I'm Dr. X, your AI growth mindset coach. How can I help you explore your potential today?"}
    ]

# Function to call Gemini API with exponential backoff for chat
def get_gemini_chat_response_with_retry(chat_history_for_gemini, max_retries=5, initial_delay=1.0):
    payload = {
        "contents": chat_history_for_gemini,
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

# --- Dr. X Chat Interface ---
st.header("💬 Talk to Dr. X")
st.markdown("Ask Dr. X anything about growth mindset, challenges, mistakes, or your personal growth journey!")

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask Dr. X about your growth...", key="drx_chat_input"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Construct the full chat history for Gemini API, including system instruction
    gemini_chat_history = []
    # System instruction as the first user message for context
    gemini_chat_history.append({"role": "user", "parts": [{"text": "You are Dr. X, a friendly, encouraging, and knowledgeable AI growth mindset coach for middle and high school students. Your goal is to provide supportive, actionable advice on embracing challenges, learning from mistakes, and fostering a growth mindset. Keep responses concise and inspiring. Always maintain a positive and supportive tone."}]})
    # Acknowledge the system instruction from the model's side
    gemini_chat_history.append({"role": "model", "parts": [{"text": "Understood. I'm ready to help you on your growth journey!"}]})

    # Append actual chat history
    for msg in st.session_state.chat_history:
        # Ensure roles are 'user' or 'model' for Gemini API
        role = "user" if msg["role"] == "user" else "model"
        gemini_chat_history.append({"role": role, "parts": [{"text": msg["content"]}]})

    # Get assistant response
    with st.spinner("Dr. X is thinking..."):
        assistant_response = get_gemini_chat_response_with_retry(gemini_chat_history)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})


# --- Journaling Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Your Growth Journal</h2>', unsafe_allow_html=True)
challenge_text = st.text_area("Describe a challenge you're facing:", height=100, key="journal_challenge_text")
effort_taken = st.text_area("What effort have you made so far?", height=100, key="journal_effort_taken")
mistake_text = st.text_area("Describe a mistake you’ve made:", height=100, key="journal_mistake_text")
lesson_learned = st.text_area("What did you learn from that mistake?", height=100, key="journal_lesson_learned")
growth_action = st.text_input("One action you’ll take to grow this week:", "e.g., Ask for help on a tough math problem", key="journal_growth_action")

# --- Export Button ---
if st.button("📅 Download My Journal as Text File", class_name="button-style", key="download_journal_btn"):
    buffer = io.StringIO()
    buffer.write("Growth Mindset Reflection Journal\n\n")
    buffer.write(f"Challenge: {challenge_text}\n")
    buffer.write(f"Effort: {effort_taken}\n\n")
    buffer.write(f"Mistake: {mistake_text}\n")
    buffer.write(f"Lesson Learned: {lesson_learned}\n\n")
    buffer.write(f"Growth Action: {growth_action}\n")
    st.download_button(
        label="Click to download",
        data=buffer.getvalue(),
        file_name="growth_journal.txt",
        mime="text/plain",
        key="download_button_final" # Added a unique key for the download button itself
    )
st.markdown('</div>', unsafe_allow_html=True)


# --- Actionable Steps & Future Connections (Moved from previous location to be separate from journal) ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Grow Your Brain, Shape Your Future!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Your brain is like a muscle – the more you challenge it and learn from your experiences, the stronger it gets!
    This growth mindset isn't just for school; it's a superpower for life.
    It helps you tackle new technologies, solve complex problems, and innovate in fields like:
</p>
<ul class="list-disc list-inside text-gray-700 space-y-2 mb-4">
    <li>**Artificial Intelligence & Machine Learning:** Learning new algorithms and debugging code.</li>
    <li>**Biotechnology & Medicine:** Discovering new treatments and understanding complex biological systems.</li>
    <li>**Engineering & Robotics:** Designing, building, and refining innovative solutions.</li>
    <li>**Creative Arts & Design:** Pushing boundaries and developing unique styles.</li>
</ul>
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Every time you persist, every time you learn from a mistake, you're building the skills you'll need to excel in these future-forward careers!
</p>
""", unsafe_allow_html=True)

# The "Your Growth Plan" input is now part of the journal section above,
# but the motivational text remains here.
st.markdown(f"""
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        Remember: Consistency is key to growth! You've got this! 💪
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- Footer ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Developed by Xavier Honablue M.Ed for CognitiveCloud.ai Education</p>
</div>
""", unsafe_allow_html=True)
