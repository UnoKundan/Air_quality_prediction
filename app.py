import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Air Quality Prediction", page_icon="🍃", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load("air_quality_model.pkl")

st.title("🍃 Air Quality Prediction Dashboard")

model = load_model()

col1, col2, col3 = st.columns(3)

with col1:
    pt08_s1 = st.number_input("PT08.S1(CO)", value=1000.0)
    nmhc = st.number_input("NMHC(GT)", value=150.0)
    c6h6 = st.number_input("C6H6(GT)", value=10.0)
    pt08_s2 = st.number_input("PT08.S2(NMHC)", value=900.0)

with col2:
    nox = st.number_input("NOx(GT)", value=200.0)
    pt08_s3 = st.number_input("PT08.S3(NOx)", value=800.0)
    no2 = st.number_input("NO2(GT)", value=100.0)
    pt08_s4 = st.number_input("PT08.S4(NO2)", value=1400.0)

with col3:
    pt08_s5 = st.number_input("PT08.S5(O3)", value=1000.0)
    t = st.number_input("T", value=20.0)
    rh = st.number_input("RH", value=50.0)
    ah = st.number_input("AH", value=1.0)

if st.button("Predict"):
    df = pd.DataFrame([{
        'PT08.S1(CO)': pt08_s1,
        'NMHC(GT)': nmhc,
        'C6H6(GT)': c6h6,
        'PT08.S2(NMHC)': pt08_s2,
        'NOx(GT)': nox,
        'PT08.S3(NOx)': pt08_s3,
        'NO2(GT)': no2,
        'PT08.S4(NO2)': pt08_s4,
        'PT08.S5(O3)': pt08_s5,
        'T': t,
        'RH': rh,
        'AH': ah
    }])

    prediction = model.predict(df)[0]

    st.success("Prediction Completed")
    st.metric("Predicted CO(GT)", f"{prediction:.4f}")
