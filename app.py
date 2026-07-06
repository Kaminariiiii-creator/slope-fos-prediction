import streamlit as st
import pandas as pd
import joblib

st.title("AutoSlope (智動坡)")
st.write("Input the parameters to instantly predict the Factor of Safety (FoS) for a soil slope")

col1, col2 = st.columns(2)

col1, col2 = st.columns(2)

with col1:
    height = st.number_input(
        "Height (m)", 
        min_value=5.0, 
        step=0.5, 
        format="%.2f"
    )
    angle = st.number_input(
        "Angle (degree)", 
        min_value=20, 
        step=1, 
        format="%d"
    )
    surcharge = st.number_input(
        "Surcharge (kPa)", 
        min_value=0.0, 
        step=1.0, 
        format="%.1f"
    )

with col2:
    phi = st.number_input(
        "phi' (degree)", 
        min_value=30.0,        # ← 改做 30.0 (float)
        step=0.5, 
        format="%.1f"
    )
    c = st.number_input(
        "c' (kPa)", 
        min_value=0.0, 
        step=0.5, 
        format="%.2f"
    )
    gw = st.selectbox("Groundwater", ["Dry", "One-Third"])
    gw_encoded = 0 if gw == "Dry" else 1

if st.button("Predict FoS"):
    model = joblib.load("FoS_XGBoost_Fill_with_GW.joblib")
    input_data = pd.DataFrame({
        'Height_m': [height],
        'Angle_deg': [angle],
        'Surcharge_kPa': [surcharge],
        'phi_deg': [phi],
        'c_kPa': [c],
        'GW_encoded': [gw_encoded]
    })
    fos = model.predict(input_data)[0]
    st.success(f"Predicted FoS = {fos:.4f}")
    
