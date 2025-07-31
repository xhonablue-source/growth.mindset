import streamlit as st

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

# --- Introduction Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Welcome, Future Achiever!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Have you ever felt stuck on a tough problem? Or thought, "I'm just not good at this"?
    That's a common feeling, but here at CognitiveCloud.ai, we believe in the power of a **Growth Mindset**!
    This means understanding that your abilities and intelligence can grow and develop through dedication and hard work.
    It's not about being "smart" or "not smart"; it's about **effort, learning, and perseverance**.
</p>
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        "The power of 'not yet'!" - Carol Dweck
    </p>
    <p style='color: #4CAF50;'>
        Instead of saying "I can't do it," try "I can't do it *yet*!" This simple shift opens up possibilities for learning and improvement.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# --- Challenge & Effort Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Embrace Challenges!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Challenges aren't roadblocks; they're opportunities for your brain to get stronger!
    When you face something difficult, it means you're pushing your boundaries, and that's exactly how you learn and grow.
</p>
""", unsafe_allow_html=True)

st.subheader("Your Challenge Journal:")
challenge_text = st.text_area("What is a challenge you're currently facing (in math, school, or life)?", height=100)
effort_taken = st.text_area("What effort have you put into overcoming this challenge so far?", height=100)

if st.button("Reflect on My Challenge", key="reflect_challenge_btn", help="Click to see a growth mindset perspective."):
    if challenge_text and effort_taken:
        st.markdown(f"""
        <div class="highlight-box">
            <p style='font-weight: bold; color: #388E3C;'>
                Great job identifying your challenge! 🎉
            </p>
            <p style='color: #4CAF50;'>
                It's inspiring to see the effort you've already put into "{challenge_text}".
                Remember, every bit of effort, even small steps, builds your strength and understanding.
                Keep going! What's one more small step you can take today?
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please describe your challenge and effort to reflect.")
st.markdown('</div>', unsafe_allow_html=True)


# --- Learning from Mistakes Section ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">Mistakes Are Your Best Teachers!</h2>', unsafe_allow_html=True)
st.markdown("""
<p style='font-size: 1.1rem; line-height: 1.6;'>
    Nobody is perfect, and making mistakes is a natural and essential part of learning.
    Think of a mistake as a clue that helps you understand something better.
    It's not a sign of failure, but a stepping stone to success!
</p>
""", unsafe_allow_html=True)

st.subheader("My Mistake, My Lesson:")
mistake_text = st.text_area("Describe a mistake you recently made (e.g., in a math problem, a project).", height=100)
lesson_learned = st.text_area("What did you learn from this mistake? How will it help you next time?", height=100)

if st.button("Discover My Lesson", key="discover_lesson_btn", help="Click to see the positive side of your mistake."):
    if mistake_text and lesson_learned:
        st.markdown(f"""
        <div class="highlight-box">
            <p style='font-weight: bold; color: #388E3C;'>
                That's fantastic self-reflection! 🌟
            </p>
            <p style='color: #4CAF50;'>
                By understanding "{mistake_text}" and learning "{lesson_learned}", you've turned a challenge into a powerful learning experience.
                This is the essence of a growth mindset! Every mistake helps you refine your approach.
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please describe your mistake and what you learned from it.")
st.markdown('</div>', unsafe_allow_html=True)


# --- Actionable Steps & Future Connections ---
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

st.subheader("Your Growth Plan:")
growth_action = st.text_input("What's one specific action you will take this week to practice your growth mindset?", "e.g., Ask for help on a difficult math problem.")
st.markdown(f"""
<div class="highlight-box">
    <p style='font-weight: bold; color: #388E3C;'>
        Action Plan:
    </p>
    <p style='color: #4CAF50;'>
        This week, I will focus on: "{growth_action}".
        Remember, consistency is key to growth! You've got this! 💪
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
