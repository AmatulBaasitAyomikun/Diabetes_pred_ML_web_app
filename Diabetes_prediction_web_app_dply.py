# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:44:25 2025

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav','rb'))

# Prediction function

def diabetes_prediction(input_data):
    
    # Change input_data to numpy array
    input_data_as_array = np.asarray(input_data)

    # Reshape the input_data array
    input_data_reshaped = input_data_as_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]):
      return 'This user is diabetic'
    else:
      return 'This user is not diabetic'

def main():
    
    # streamlit interface
    st.title("Diabetes Prediction Web App")
    
    # Input data from users
    
    Pregnancies = st.number_input('Number of pregnancies')
    Glucose = st.number_input('Blood Glucose level')
    BloodPressure = st.number_input('Diastolic BP value')
    SkinThickness = st.number_input('Skin thickness measurement')
    Insulin = st.number_input('Blood Insulin level')
    BMI = st.number_input('Body mass index value')
    DiabetesPedigreeFunction = st.number_input('Family history of Diabetes index')
    Age = st.number_input('Age of the user')
    
    # code for diagnosis prediction
    
    diagnosis = " "
    if st.button('Check Diabetes Status'):
        diagnosis = diabetes_prediction([Pregnancies,
                                         Glucose,
                                         BloodPressure,
                                         SkinThickness,
                                         Insulin,
                                         BMI,
                                         DiabetesPedigreeFunction,
                                         Age
                                         ])
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
        
  
    
  
    