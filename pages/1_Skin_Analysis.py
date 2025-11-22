import streamlit as st
from PIL import Image

st.title("📸 Skin Analysis")

uploaded_file = st.file_uploader("Upload your face image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    st.write("🔍 Analyzing your skin...")

    # TODO: Add model inference
    results = {
        "Skin Type": "Oily",
        "Concerns": ["Acne", "Pigmentation"],
        "Skin Tone": "Medium"
    }

    st.json(results)
