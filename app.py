import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load("Student_score.pkl")
scaler = joblib.load("scaler.pkl")

study_hrs = st.number_input("Study Hours", min_value=0, max_value=100, step=1)
attendance = st.number_input("Attendance", min_value=10, max_value=100, step=1)
past_score = st.number_input("Past Score", min_value=10, max_value=100, step=1)
internet = st.selectbox("Internet", ["Yes", "No"])
sleep_hrs = st.number_input("Sleep Hours", min_value=0, max_value=24,step=1)

if st.button("Submit"):

    train_col = ['Study Hours', 'Attendance', 'PastScore', 'Internet', 'SleepHours']

    input_df = pd.DataFrame({
        "Study Hours": [study_hrs],
        "Attendance": [attendance],
        "PastScore": [past_score],
        "Internet": [internet],
        "SleepHours": [sleep_hrs]
        }
    )

    le = LabelEncoder()
    input_df["Internet"] = input_df["Internet"].map({
    "No": 0,
    "Yes": 1 
    })

    input_df = input_df.reindex(columns=train_col, fill_value=0)

    input_scaler = scaler.transform(input_df)
    prediction = model.predict(input_scaler)

    if prediction[0] == 1:
        st.success("As per submitted data, the student is likely to pass.")
    else:
        st.error("As per submitted data, the student is likely to fail.")

