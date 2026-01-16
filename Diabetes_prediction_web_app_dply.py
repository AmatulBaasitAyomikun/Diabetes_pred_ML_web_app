# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:44:25 2025

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st
import os

# Get the folder where this Python file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to the model file
MODEL_PATH = os.path.join(BASE_DIR, "trained_model.sav")

# Load the model
with open(MODEL_PATH, "rb") as file:
    loaded_model = pickle.load(file)


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
    
    # FEATURE EXPLANATIONS 


    FEATURE_HELP = {
        "Pregnancies": "Number of times the person has been pregnant.",
        "Glucose": "Blood sugar level (plasma glucose). Higher can increase diabetes risk.",
        "BloodPressure": "Diastolic blood pressure (mm Hg).",
        "SkinThickness": "Triceps skin fold thickness (mm). A body fat indicator.",
        "Insulin": "2-hour serum insulin (mu U/ml).",
        "BMI": "Body Mass Index (weight/height²).",
        "DiabetesPedigreeFunction": "Family history score (genetic likelihood).",
        "Age": "Age in years. Risk generally increases with age."
    }

    with st.expander("ℹ️ What do these inputs mean? (Click to open)"):
        st.write("Each field below is a model **feature** (input). Here’s what they mean:")
        for k, v in FEATURE_HELP.items():
            st.markdown(f"- **{k}**: {v}")

    
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
        
  
    
  
    