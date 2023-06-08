# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:19:05 2023

@author: pishu
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(
    open('D:/minor projects 6 docs/trained_model.sav', 'rb'))


# creating a function for prediction

def migrane_prediction(input_data):


# changing the input_data to numpy array
   input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
   input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# standardize the input data
# std_data = scaler.transform(input_data_reshaped)
# print(std_data)

   prediction = loaded_model.predict(input_data_reshaped)
   print(prediction)

   if (prediction[0] == 0):
      return 'The person does not have migrane '
   else:
     return 'The person have migrane'


def main():
  # giving a title

    st.title('Migrane Prediction Web App')

    # getting the input data from the user
    #Age, Duration, frequency,Location, character, intensity, Nausea, Vomit, Phonophobia,photophobia,visual,sensory,Dysphasia,Dysarthria,vertigo,Tinnitus,Hypoacusis,Diplopia,Defect,Ataxia,Conscience,parathesia,DPF,Type

    Age = st.text_input(' Age ')
    Duration = st.text_input(' Duration ')
    frequency = st.text_input(' frequency ')
    Location = st.text_input(' Location ')
    character = st.text_input(' character ')
    intensity = st.text_input(' intensity ')
    Nausea = st.text_input(' Nausea ')
    Vomit = st.text_input(' Vomit ')
    Phonophobia = st.text_input(' Phonophobia ')
    photophobia = st.text_input(' photophobia ')
    visual = st.text_input(' visual ')
    sensory = st.text_input(' sensory ')
    Dysphasia = st.text_input(' Dysphasia')
    Dysarthria = st.text_input(' Dysarthria ')
    Tinnitus = st.text_input(' Tinnitus ')
    Hypoacusis = st.text_input(' Hypoacusis ')
    Diplopia = st.text_input(' Diplopia ')
    Ataxia = st.text_input(' Ataxia ')
    Conscience = st.text_input(' Conscience ')
    parathesia = st.text_input(' parathesia ')
    DPF = st.text_input(' DPF ')
    Type = st.text_input(' Type ')

   # code for prediction
    diagnosis = ''
   
   # creating a button for prediction
    if st.button('Migrane Test Result'):
          diagnosis = migrane_prediction([Age, Duration, frequency,Location, character, intensity, Nausea, Vomit, Phonophobia,photophobia,visual,sensory,Dysphasia,Dysarthria,vertigo,Tinnitus,Hypoacusis,Diplopia,Defect,Ataxia,Conscience,parathesia,DPF])
    
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()