import streamlit as st

st.set_page_config(
    page_title="AI Skincare System", 
    layout="wide",
    page_icon="💆‍♀️"
)

st.title("💆‍♀️ Radiance - AI Skincare Recommendation System")
st.markdown("---")

st.write("### 📍 Navigation")
st.write("Use the sidebar on the left to navigate between pages:")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📸 Skin Analysis")
    st.write("Upload your face image or use webcam for AI-powered skin analysis")
    st.write("→ Go to: **Skin Analysis** page in sidebar")

with col2:
    st.subheader("📘 Product History")
    st.write("Track your skincare products and their effects")
    st.write("→ Go to: **Product History** page in sidebar")

with col3:
    st.subheader("✨ Recommendations")
    st.write("Get personalized skincare recommendations")
    st.write("→ Go to: **Recommendations** page in sidebar")

st.markdown("---")
st.subheader("🚀 How It Works")

steps = [
    "1. **Skin Analysis**: Use webcam or upload photo for face detection and skin analysis",
    "2. **Product History**: Record products you've used and their effects", 
    "3. **AI Recommendations**: Get personalized product suggestions based on your skin profile"
]

for step in steps:
    st.write(step)

st.info("💡 Start with Skin Analysis to unlock personalized recommendations!")