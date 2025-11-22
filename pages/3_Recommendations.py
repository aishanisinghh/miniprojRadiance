import streamlit as st
import pandas as pd

st.title("✨ Personalized Skincare Recommendations")

# Check if skin analysis was done
if 'skin_analysis' in st.session_state and st.session_state.skin_analysis:
    st.success("✅ Using your skin analysis for personalized recommendations!")
    
    # Display analysis results
    for face, analysis in st.session_state.skin_analysis.items():
        with st.expander(f"📊 {face.replace('_', ' ').title()} Analysis"):
            st.json(analysis)
    
    # Generate recommendations based on analysis
    st.subheader("🎯 Recommended Products")
    
    # Example recommendations based on skin type
    skin_type = list(st.session_state.skin_analysis.values())[0].get("Skin Type", "Unknown")
    
    if skin_type == "Oily":
        recommendations = [
            {"Product": "Niacinamide Serum", "Price": "₹249", "Benefit": "Oil Control", "Rating": "4.5⭐"},
            {"Product": "Salicylic Acid Cleanser", "Price": "₹349", "Benefit": "Acne Treatment", "Rating": "4.3⭐"},
            {"Product": "Oil-Free Moisturizer", "Price": "₹299", "Benefit": "Hydration", "Rating": "4.6⭐"}
        ]
    elif skin_type == "Dry":
        recommendations = [
            {"Product": "Hyaluronic Acid Serum", "Price": "₹299", "Benefit": "Deep Hydration", "Rating": "4.7⭐"},
            {"Product": "Ceramide Cream", "Price": "₹399", "Benefit": "Moisture Barrier", "Rating": "4.5⭐"},
            {"Product": "Gentle Cream Cleanser", "Price": "₹249", "Benefit": "Non-Drying", "Rating": "4.4⭐"}
        ]
    else:
        recommendations = [
            {"Product": "Vitamin C Serum", "Price": "₹349", "Benefit": "Brightening", "Rating": "4.6⭐"},
            {"Product": "SPF 50 Sunscreen", "Price": "₹299", "Benefit": "UV Protection", "Rating": "4.8⭐"},
            {"Product": "AHA/BHA Toner", "Price": "₹399", "Benefit": "Exfoliation", "Rating": "4.4⭐"}
        ]
    
    # Display recommendations as a nice table
    df = pd.DataFrame(recommendations)
    st.dataframe(df, use_container_width=True)
    
    st.info("💡 These recommendations are based on your skin analysis. Complete your product history for more personalized suggestions!")
    
else:
    st.warning("⚠️ Please complete your Skin Analysis first to get personalized recommendations!")
    st.info("Go to the 'Skin Analysis' page to upload/take a photo of your face for analysis.")

# Always show the product history integration
st.markdown("---")
st.subheader("📘 Based on Your Product History")

# Example table (will be populated from product history)
data = {
    "Product": ["Niacinamide Serum", "Salicylic Acid Cleanser"],
    "Price": ["₹249", "₹349"],
    "Your Rating": ["5⭐", "3⭐"],
    "Effect": ["Improved", "Irritated"]
}

df_history = pd.DataFrame(data)
st.table(df_history)

st.write("💡 **Tip**: Rate more products in 'Product History' to improve recommendations!")