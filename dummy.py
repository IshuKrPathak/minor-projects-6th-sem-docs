# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 00:47:46 2023

@author: pishu
"""

import streamlit as st
import pandas as pd

st.title("Enter Symptoms to check the probabilities of a diseases ")
# Load the CSV file
st.cache_data
def load_data():
    data = pd.read_csv("D:\minor projects 6 docs\main_file.csv")
    return data

data = load_data()

# Create a text input for the user to enter a value
value_input = st.text_input('Enter a Symptom 1')
filtered_data = data[data['symptom1'] == value_input] 
st.write(filtered_data)

value_input = st.text_input('Enter Symptom 2')
filtered_data = data[data['symptom2'] == value_input] 
st.write(filtered_data)

value_input = st.text_input('Enter a Symptom 3')
filtered_data = data[data['symptom3'] == value_input] 
st.write(filtered_data)

value_input = st.text_input('Enter a Symptom 4')
filtered_data = data[data['symptom4'] == value_input] 
st.write(filtered_data)

# Display the filtered data
if not filtered_data.empty:
    st.write(filtered_data)
else:
    st.write('Enter in Small letters')