import streamlit as st
import pandas as pd
import numpy as np
import joblib
from scipy.stats import skew  # ✅ Correct import
# ❌ Removed unused import: from scipy.ndimage import label

# Load the trained model
model = joblib.load("Nadi_Diabetes_Model.pkl")

# UI Header
st.title("🧬 Nadi Pulse Diabetes Predictor")
col1, col2, col3 = st.columns(3)

# User inputs
with col1:
    name = st.text_input("Enter Your Name")
with col2:
    age = st.number_input("Enter Your Age ", min_value=1, max_value=120)
with col3:
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])

st.write("Upload your optical sensor `nadi_data.txt` file to predict diabetes.")

uploaded_file = st.file_uploader("Choose a nadi_data.txt file", type="txt")

# Feature extraction
def extract_features_from_txt(txt_bytes, age):
    content = txt_bytes.decode("utf-8").splitlines()
    pulse_data = []

    for line in content:
        if line.strip().lower().startswith("start"):
            continue
        try:
            values = list(map(int, line.strip().split(",")))
            if len(values) == 3:
                pulse_data.append(values)
        except:
            continue

    if not pulse_data:
        return None

    pulse_array = np.array(pulse_data)
    ch1, ch2, ch3 = pulse_array[:, 0], pulse_array[:, 1], pulse_array[:, 2]

    features = {
        "ch1_mean": np.mean(ch1),
        "ch1_std": np.std(ch1),
        "ch1_min": np.min(ch1),
        "ch1_max": np.max(ch1),
        "ch1_skew": skew(ch1),

        "ch2_mean": np.mean(ch2),
        "ch2_std": np.std(ch2),
        "ch2_min": np.min(ch2),
        "ch2_max": np.max(ch2),
        "ch2_skew": skew(ch2),

        "ch3_mean": np.mean(ch3),
        "ch3_std": np.std(ch3),
        "ch3_min": np.min(ch3),
        "ch3_max": np.max(ch3),
        "ch3_skew": skew(ch3),

        "age": age
    }

    return pd.DataFrame([features])

# Prediction
if uploaded_file is not None:
    if age <= 0 or name.strip() == "":
        st.warning("⚠️ Please enter valid Name and Age before prediction.")
    else:
        bytes_data = uploaded_file.read()
        feature_df = extract_features_from_txt(bytes_data, age)

        if feature_df is None:
            st.error("❌ Invalid file format or no valid pulse data found.")
        else:
            if st.button("👩🏻‍⚕️ Predict"):
                prediction = model.predict(feature_df)[0]

                # Multi-class prediction handling
                if prediction == 1:
                    label = "🤒 DIABETES - NOT CONTROL -- *UNHEALTHY*"
                elif prediction == 0:
                    label = "🤒 ANEMIA AND OTHERS -- *UNHEALTHY*"
                else:
                    label = "✅ DIABETES - UNDER CONTROL -- *HEALTHY*"

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.subheader(f"Patient: {name}")
                with col2:
                    st.subheader(f"Age: {age}")
                with col3:
                    st.subheader(f"Gender: {gender}")
                st.header("👩🏻‍⚕️ DOCTOR COMMENT")
                st.header(label)
                # st.subheader("📊 Extracted Features")
                # st.dataframe(feature_df)
