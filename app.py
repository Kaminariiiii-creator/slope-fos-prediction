import streamlit as st
import pandas as pd
import joblib

st.title("Soil Slope FoS Prediction Model")
st.write("Input the parameters to instantly predict the Factor of Safety (FoS) for a soil slope")

col1, col2 = st.columns(2)
with col1:
    height = st.number_input("Height (m)", value=0, min_value=1)
    angle = st.number_input("Angle (degree)", value=0, min_value=1)
    surcharge = st.number_input("Surcharge (kPa)", value=0.0, min_value=0.0)

with col2:
    phi = st.number_input("phi' (degree)", value=0, min_value=1)
    c = st.number_input("c' (kPa)", value=0, min_value=0.0)
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
    st.success(f"Predicted FoS = **{fos:.4f}**")
    
