# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 3:47:32 2023

@author: pishu
"""

import csv
import streamlit as st

st.title("Enter Symptoms to check the probabilities of a disease ")

text_input1 = st.text_input('symptom 1 ')
with open("D:\minor projects 6 docs\main_file.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = []
    if text_input1:
        for row in csv_reader:
            for i in range(len(row)):
                if text_input1 in row[i]:
                    data.append(row)
                    st.write(row[0])


text_input2 = st.text_input('symptom 2 ')
f = []
if text_input2:
    for row in data:
        for i in range(len(row)):
            if text_input2 in row[i]:
                f.append(row)
                st.write(row[0])

text_input3 = st.text_input('symptom 3 ')
g = []
if text_input3:
  for row in f:
     for i in range(len(row)):
        if text_input3 in row[i]:
            g.append(row)
            st.write(row[0])


text_input4 = st.text_input('symptom 4 ')
h = []
if text_input4:
  for row in g:
    for i in range(len(row)):
        if text_input4 in row[i]:
            h.append(row)
            st.write(row[0])
