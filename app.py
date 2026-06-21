import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="IUBBACKEND - Portal Update",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. ZERO Indentation HTML string for Bulletproof Rendering
html_string = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* Elegant, Deep Animated Background */
.stApp {
background: linear-gradient(-45deg, #020617, #1e1b4b, #0f172a, #170f23);
background-size: 400% 400%;
animation: gradientBG 15s ease infinite;
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
color: #ffffff;
}
@keyframes gradientBG {
0% { background-position: 0% 50%; }
50% { background-position: 100% 50%; }
100% { background-position: 0% 50%; }
}

/* Flex Container to Center the Card Perfectly */
.container {
display: flex;
justify-content: center;
align-items: center;
min-height: 85vh;
}

/* Sophisticated Glassmorphism Card with Fade-In Animation */
.card {
background: rgba(255, 255, 255, 0.03);
backdrop-filter: blur(24px);
-webkit-backdrop-filter: blur(24px);
border: 1px solid rgba(255, 255, 255, 0.08);
border-radius: 24px;
padding: 50px 40px;
text-align: center;
max-width: 500px;
width: 100%;
box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
animation: fadeInUp 1s ease-out forwards;
opacity: 0;
transform: translateY(30px);
}
@keyframes fadeInUp {
to { opacity: 1; transform: translateY(0); }
}

/* Refined Typography */
.title {
font-size: 2.6rem;
font-weight: 800;
letter-spacing: -1px;
margin-bottom: 8px;
background: linear-gradient(135deg, #e0e7ff, #818cf8, #c084fc);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}

.subtitle {
color: #94a3b8;
font-size: 1.1rem;
margin-bottom: 30px;
}

/* Feature Box */
.features {
background: rgba(0, 0, 0, 0.2);
border-radius: 16px;
padding: 20px;
margin-bottom: 30px;
border: 1px solid rgba(255, 255, 255, 0.05);
}
.features p {
margin: 8px 0;
color: #cbd5e1;
font-size: 1rem;
}
.highlight {
color: #38bdf8;
font-weight: 600;
}

/* Warning Message */
.warning {
color: #fca5a5;
font-size: 0.85rem;
margin-bottom: 35px;
padding: 12px;
background: rgba(248, 113, 113, 0.1);
border: 1px solid rgba(248, 113, 113, 0.2);
border-radius: 12px;
}

/* Primary Action Button */
.btn-primary {
display: block;
background: linear-gradient(135deg, #4f46e5, #9333ea);
color: #ffffff !important;
text-decoration: none;
font-size: 1.15rem;
font-weight: 600;
padding: 16px 32px;
border-radius: 50px;
transition: all 0.3s ease;
box-shadow: 0 10px 25px -5px rgba(147, 51, 234, 0.4);
margin-bottom: 20px;
}
.btn-primary:hover {
transform: translateY(-3px);
box-shadow: 0 15px 30px -5px rgba(147, 51, 234, 0.6);
}

/* Secondary Action Button (Small) */
.btn-secondary {
display: inline-block;
color: #64748b !important;
text-decoration: none;
font-size: 0.9rem;
font-weight: 500;
transition: all 0.2s ease;
}
.btn-secondary:hover {
color: #e2e8f0 !important;
text-decoration: underline;
}
</style>

<div class="container">
<div class="card">
<div class="title">IUBBACKEND</div>
<div class="subtitle">The Result Portal, completely new design.</div>

<div class="features">
<p><span class="highlight">⚡ Faster Performance</span></p>
<p><span class="highlight">🎨 Modernized UI Experience</span></p>
<p style="margin-top: 15px; font-weight: bold; color: #a7f3d0;">✨ Create your new account!</p>
</div>

<div class="warning">
⚠️ Note: Previous accounts will not work. A new account is required.
</div>

<a href="https://iubbackend.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-primary">
See Results with New Portal
</a>

<a href="https://iub-old.streamlit.app" target="_blank" rel="noopener noreferrer" class="btn-secondary">
Use Old Website
</a>
</div>
</div>
"""

# 3. Inject the UI
st.markdown(html_string, unsafe_allow_html=True)
