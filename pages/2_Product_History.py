import streamlit as st
import pandas as pd

st.title("📘 Your Product History")

product_name = st.text_input("Product name")
rating = st.slider("How did it work?", 1, 5)
effect = st.selectbox("Effects on your skin", ["Improved", "No change", "Irritated"])

if st.button("Save"):
    st.success("Saved ✔")

    # TODO: Save to CSV or database
