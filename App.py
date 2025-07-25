import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model
with open('fake_job_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🕵️‍♂️ Fake Job Detection App")
st.markdown("Enter job details below to check if it's **Fake** or **Real**")

# Row 1: Job Description (Full Width)
description = st.text_area("Job Description", height=200)

# Row 2: Employment Type and Industry (2 columns)
col1, col2 = st.columns(2)
with col1:
    employment_type = st.selectbox("Employment Type", ['Full-time', 'Part-time', 'Contract', 'Temporary', 'Unknown'])
with col2:
    industry = st.selectbox("Industry", [
        'Information Technology', 'Marketing', 'Healthcare', 'Education',
        'Finance', 'Engineering', 'Hospitality', 'Retail',
        'Telecommunications', 'Consulting', 'Legal', 'Administrative',
        'Media', 'Unknown'
    ])

# Row 3: Telecommuting, Logo, Questions (3 columns)
col3, col4, col5 = st.columns(3)
with col3:
    telecommuting = st.selectbox("Telecommuting?", [0, 1])
with col4:
    has_company_logo = st.selectbox("Company Logo?", [0, 1])
with col5:
    has_questions = st.selectbox("Screening Questions?", [0, 1])

# Predict button
if st.button("Predict"):
    input_data = {
        'description': [description],
        'employment_type': [employment_type],
        'industry': [industry],
        'telecommuting': [telecommuting],
        'has_company_logo': [has_company_logo],
        'has_questions': [has_questions]
    }

    input_df = pd.DataFrame(input_data)

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ This job posting seems **FAKE**.")
    else:
        st.success("✅ This job posting seems **REAL**.")
