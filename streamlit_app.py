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
    "UI/UX",
    "Teamwork",
    "MS Office",
    "Communication skills",
    "Problem-solving skills",
    "Basic programming (C, Python)"
]

for skill in skills:
    st.write(f"- {skill}")

st.markdown("---")

# Projects
st.header("💻 Projects")

st.subheader("Beatawre - AI Powered Heart Attack Prediction and Detection App")
st.write("""
- Developed a **cross-platform mobile app** using **React Native** for real-time heart attack detection and prediction.  
- Implemented clean and responsive UI with **Tailwind CSS**, ensuring accessibility and smooth user experience across devices.  
- Integrated Python-based **machine learning models** via APIs to analyze health data (ECG, heart rate, oxygen levels).  
- Used **Twilio API** for instant emergency alerts (to hospitals, relatives, ambulance services) with live location sharing.  
- Added AI-driven predictive analysis to provide early warnings, lifestyle suggestions, and preventive medical insights.  
""")
  

st.markdown("---")

# Education
st.header("🎓 Education")
st.write("""
- **B.E. Computer Science and Engineering** (Ongoing) - KCG College of Technology, Chennai - 83.4%  
- **Higher Secondary** - Sairam Vidyalaya - 90% (2022)  
- **SSLC** - Sairam Vidyalaya - 85% (2020)  
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

st.markdown("---")

# Footer
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        © 2025 Karunya
    </div>
    """,
    unsafe_allow_html=True
)

