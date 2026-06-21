import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="IUBBACKEND - Portal Update",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Animations and Modern UI
custom_css = """
<style>
    /* Hide default Streamlit elements for a clean landing page */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        /* Animated Gradient Background */
        background: linear-gradient(-45deg, #0f172a, #1e293b, #334155, #020617);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: white;
        font-family: 'Inter', sans-serif;
    }

    /* Background Animation Keyframes */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Centered Glassmorphism Card with Floating Animation */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px 30px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        animation: float 6s ease-in-out infinite;
        margin-top: 5vh;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0px); }
    }

    /* Typography */
    .title-text {
        font-size: 2.8rem !important;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    .subtitle-text {
        font-size: 1.5rem;
        font-weight: 400;
        color: #e2e8f0;
        margin-bottom: 25px;
    }

    .tags {
        font-size: 0.85rem;
        color: #94a3b8;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 30px;
        display: flex;
        justify-content: center;
        gap: 15px;
    }

    .highlight-box {
        background: rgba(56, 189, 248, 0.1);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 15px;
        margin: 20px 0;
    }

    .features {
        font-size: 1.1rem;
        color: #cbd5e1;
        margin-bottom: 10px;
    }

    .create-account {
        color: #fbbf24;
        font-weight: 700;
        font-size: 1.2rem;
        margin-top: 15px;
    }

    .warning-text {
        color: #f87171;
        font-size: 0.9rem;
        font-weight: 500;
        margin-top: 10px;
        margin-bottom: 35px;
    }

    /* Animated Glowing Button */
    .glow-button {
        display: inline-block;
        text-decoration: none;
        color: #ffffff !important;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899, #3b82f6);
        background-size: 300%;
        padding: 16px 45px;
        font-size: 1.3rem;
        font-weight: bold;
        border-radius: 50px;
        transition: all 0.4s ease-in-out;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
        animation: pulse-border 2s infinite;
    }

    .glow-button:hover {
        background-position: 100%;
        transform: scale(1.05) translateY(-3px);
        box-shadow: 0 8px 30px rgba(139, 92, 246, 0.7);
    }

    @keyframes pulse-border {
        0% { box-shadow: 0 0 0 0 rgba(139, 92, 246, 0.7); }
        70% { box-shadow: 0 0 0 15px rgba(139, 92, 246, 0); }
        100% { box-shadow: 0 0 0 0 rgba(139, 92, 246, 0); }
    }
</style>
"""

# Inject the CSS
st.markdown(custom_css, unsafe_allow_html=True)

# 3. HTML Layout Structure
html_content = """
<div class="glass-card">
    <div class="title-text">IUBBACKEND Result Portal</div>
    <div class="subtitle-text">We have updated our portal! 🚀</div>
    
    <div class="tags">
        <span>Results</span> | <span>Marks</span> | <span>Other Results</span>
    </div>
    
    <div class="highlight-box">
        <div class="features">⚡ Much Faster Performance &nbsp;•&nbsp; 🎨 Better UI Experience</div>
        <div class="create-account">✨ Create your account Now ✨</div>
    </div>
    
    <div class="warning-text">
        ⚠️ Previous accounts will not work. You must create a new one.
    </div>
    
    <a href="https://iubbackend.vercel.app" target="_top" class="glow-button">See Results</a>
</div>
"""

# Inject the UI
st.markdown(html_content, unsafe_allow_html=True)

# Optional: Add a subtle particle effect or balloons on load
st.snow() # Creates a nice falling animation effect over the dark background
