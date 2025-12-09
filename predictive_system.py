# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:40:25 2025

@author: DELL
"""

import numpy as np
import pickle

# Loading the model

loaded_model = pickle.load(open('C:/Users/DELL PC/OneDrive/Documents/MLProjects/MLproject1/trained_model.sav','rb'))

# Predictive system

input_data = (5,166,72,19,175,25.8,0.587,51)

# Change input_data to numpy array
input_data_as_array = np.asarray(input_data)

# Reshape the input_data array
input_data_reshaped = input_data_as_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]):
  print('This user is diabetic')
else:
  print('This user is not diabetic')

