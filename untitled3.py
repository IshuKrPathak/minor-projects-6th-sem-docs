# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 01:18:36 2023

@author: pishu
"""

import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache
def load_data():
    data = pd.read_csv("D:\minor projects 6 docs\main_file.csv")
    return data

data = load_data()

# Create a text input for the user to enter symptoms
symptom_input = st.text_input('Enter symptoms (separated by comma)')

# Filter the dataframe by the entered symptoms
selected_symptoms = symptom_input.split(',')
selected_data = data.loc[data[selected_symptoms].all(axis=1)]

# Display the related diseases
if not selected_data.empty:
    related_diseases = selected_data['Disease'].unique().tolist()
    st.write('Related diseases:', ', '.join(related_diseases))
else:
    st.write('No related diseases found')