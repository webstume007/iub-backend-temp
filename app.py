import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="IUBBACKEND - Portal Update",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. ZERO Indentation HTML string
# We remove all spaces at the start of these lines so Streamlit cannot trigger a code block.
html_string = """
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.stApp {
background: linear-gradient(135deg, #050505, #111827, #0f172a, #050505);
background-size: 400% 400%;
animation: gradientBG 15s ease infinite;
font-family: 'Inter', system-ui, sans-serif;
}
@keyframes gradientBG {
0% { background-position: 0% 50%; }
50% { background-position: 100% 50%; }
100% { background-position: 0% 50%; }
}
.modern-card {
background: rgba(17, 25, 40, 0.75);
backdrop-filter: blur(16px) saturate(180%);
-webkit-backdrop-filter: blur(16px) saturate(180%);
border: 1px solid rgba(255, 255, 255, 0.125);
border-radius: 20px;
padding: 60px 40px;
text-align: center;
box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
animation: floatCard 6s ease-in-out infinite;
max-width: 650px;
margin: 5vh auto;
}
@keyframes floatCard {
0% { transform: translateY(0px); }
50% { transform: translateY(-10px); }
100% { transform: translateY(0px); }
}
.gradient-title {
font-size: 3rem;
font-weight: 900;
background: linear-gradient(to right, #00f2fe, #4facfe, #00f2fe);
background-size: 200% auto;
color: #fff;
background-clip: text;
text-fill-color: transparent;
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
animation: shine 3s linear infinite;
margin-bottom: 10px;
line-height: 1.2;
}
@keyframes shine {
to { background-position: 200% center; }
}
.sub-title {
color: #9ca3af;
font-size: 1.3rem;
font-weight: 500;
margin-bottom: 30px;
}
.category-tags {
display: flex;
justify-content: center;
gap: 12px;
margin-bottom: 35px;
}
.category-tags span {
background: rgba(255, 255, 255, 0.05);
border: 1px solid rgba(255, 255, 255, 0.1);
padding: 6px 16px;
border-radius: 50px;
font-size: 0.85rem;
color: #cbd5e1;
letter-spacing: 1px;
text-transform: uppercase;
}
.info-box {
background: linear-gradient(145deg, rgba(59, 130, 246, 0.15), rgba(147, 51, 234, 0.15));
border: 1px solid rgba(99, 102, 241, 0.3);
border-radius: 16px;
padding: 25px;
margin-bottom: 30px;
}
.info-box p {
color: #e2e8f0;
font-size: 1.1rem;
margin: 8px 0;
}
.warning-msg {
color: #f87171;
font-size: 0.95rem;
display: flex;
align-items: center;
justify-content: center;
gap: 8px;
margin-bottom: 40px;
font-weight: 500;
}
.action-btn {
display: inline-block;
background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
color: #000000 !important;
text-decoration: none;
font-size: 1.25rem;
font-weight: 800;
padding: 16px 48px;
border-radius: 50px;
transition: all 0.3s ease;
box-shadow: 0 10px 20px -10px rgba(0, 201, 255, 0.7);
text-transform: uppercase;
letter-spacing: 1px;
}
.action-btn:hover {
transform: translateY(-3px) scale(1.02);
box-shadow: 0 15px 25px -10px rgba(0, 201, 255, 0.9);
}
</style>

<div class="modern-card">
<div class="gradient-title">IUBBACKEND</div>
<div class="sub-title">Result Portal Transformed 🚀</div>
<div class="category-tags">
<span>Results</span>
<span>Marks</span>
<span>Other's Result</span>
</div>
<div class="info-box">
<p>⚡ <b>Much Faster Performance</b></p>
<p>🎨 <b>Better UI Experience</b></p>
<p style="color: #4ade80; font-weight: bold; margin-top: 15px;">✨ Create your account Now</p>
</div>
<div class="warning-msg">
⚠️ Previous accounts will not work. You must create a new one.
</div>
<a href="https://iubbackend.vercel.app" target="_top" class="action-btn">
See Results
</a>
</div>
"""

# 3. Inject the UI
st.markdown(html_string, unsafe_allow_html=True)
