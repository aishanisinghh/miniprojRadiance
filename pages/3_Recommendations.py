import streamlit as st
import pandas as pd

st.title("Radiance : Personalized Skincare Recommendations")

# TODO: Load analysis results + history
st.write("Final recommendations will appear here.")

# Example table
data = {
    "Product": ["Niacinamide Serum", "Salicylic Acid Cleanser"],
    "Price": [249, 349],
    "Highlight": ["Best Price", ""]
}

df = pd.DataFrame(data)
st.table(df)
