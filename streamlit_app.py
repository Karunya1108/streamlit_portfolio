# streamlit_app.py
import streamlit as st

# Page config
st.set_page_config(page_title="Karunya", page_icon="👩‍💻", layout="wide")


# Header
st.title("KARUNYA V")
st.subheader("Software Engineer | UI/UX | Frontend Development")
st.write("📍 Madipakkam, Chennai - 91")
st.write("📞 8838734348 | 📧 [karunyavenkatachalam11@gmail.com](mailto:karunyavenkatachalam11@gmail.com)")

st.markdown("---")

# Career Objective
st.header("🎯 Career Objective")
st.write(
    "Enthusiastic Software Engineer with skills in UI/UX design and coding. "
    "Passionate about creating user-friendly applications and improving digital experiences. "
    "Proficient in design tools, front-end development, and basic programming. "
    "Strong problem-solving abilities and a keen interest in Full Stack Development and Automation."
)

st.markdown("---")

# Skills
st.header("🛠 Skills")
skills = [
    "UI/UX", "Teamwork", "MS Office", "Communication skills",
    "Problem-solving skills", "Basic programming (C, Python)"
]
st.write(", ".join(skills))

st.markdown("---")

# Projects
st.header("💻 Projects")

st.subheader("Beatawre - AI Powered Heart Attack Prediction and Detection App")
st.write("""
- Developed a heart attack detection and prediction system using Python and ML models.  
- Integrated **Twilio API** for emergency alerts with live location.  
- Designed interactive UI with HTML, CSS, JS.  
- AI-driven predictive analysis with lifestyle recommendations.  
👉 [GitHub Repository](https://github.com/Karunya1108/Beataware.git)
""")

st.subheader("Dhanam - Smart Food Management App")
st.write("""
- Built with Python, HTML, CSS, JS + MySQL backend.  
- Real-time location tracking for food pickup/distribution.  
- RESTful APIs + secure authentication.  
- Connects donors with NGOs/old-age homes to reduce food waste.  
👉 [GitHub Repository](https://github.com/Karunya1108/Dhanam.git)
""")

st.markdown("---")

# Education
st.header("🎓 Education")
st.write("""
- **B.E. Computer Science and Engineering** (Ongoing) — KCG College of Technology, Chennai — 83.4%  
- **Higher Secondary** — Sairam Vidyalaya — 90% (2022)  
- **SSLC** — Sairam Vidyalaya — 85% (2020)  
""")

st.markdown("---")

# Certifications
st.header("📜 Certifications")
st.write("""
- 1 month internship on Web Development (Technohacks)  
- MongoDB course certificate  
- NPTEL course on Programming in Java  
- 3 months online internship on UI/UX (Mitbots)  
""")


