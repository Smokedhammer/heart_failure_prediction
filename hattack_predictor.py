# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 16:17:01 2023

@author: soham
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import sklearn

def predict(data):
    clf = joblib.load("clf.sav")
    data=np.array(data).reshape(1,-1)
    return clf.predict(data)



st.title("Mortality predictor")

st.header("Using heart attack data to predict the possibility of you dying in the said follow up period")

st.subheader("Kindly enter your details so that we can give you your predictions")

first_name,last_name = st.columns(2)

f_name=first_name.text_input("First Name")
l_name=last_name.text_input("Last Name")

button=st.button("Start")

if button:
    st.write(f"Welcome {f_name}")

#####################################

# now we let the user pass in parameters 

# Age, Anaemia, Creatnine_phosphokinase,diabetes,
# ejection_fraction,high_blood_pressure,platelets,
# Serum_creatinine, serum_sodium, sex, smoking
# time, Death_event (target)

#For anaemia,diabetes,high_blood_pressure,sex,smoking we need to use a dict

yes_no_bool = {"Yes":1,"No":0}
male_female_bool = {"Male":1,"Female":0}

st.write("-------------------------------------------")

age,anaemia,creatinine_phosphokinase = st.columns(3)

age = age.number_input("Enter your age",min_value=10.00,max_value=100.00) # Maybe add some limits here
anaemia = anaemia.radio("Do you have anaemia",["Yes","No"])
anaemia = yes_no_bool[anaemia]

creatinine_phosphokinase= creatinine_phosphokinase.number_input("CPK enzyme levels (mcg/L)",step=1)


st.write("---------------------------------------------")

diabetes,ejection_fraction,high_blood_pressure = st.columns(3)

diabetes = diabetes.radio("Do you have diabetes",["Yes","No"])
diabetes = yes_no_bool[diabetes]

ejection_fraction = ejection_fraction.number_input("Percentage of blood leaving",step=1,min_value=0,max_value=100)
high_blood_pressure = high_blood_pressure.radio("Do you have Hypertension",["Yes","No"])
high_blood_pressure = yes_no_bool[high_blood_pressure]


st.write("---------------------------------------------")

platelets,serum_creatinine,serum_sodium = st.columns(3)

platelets = platelets.number_input("Platelets in the blood")
serum_creatinine= serum_creatinine.number_input("Level of creatinine (mg/dL)")
serum_sodium=serum_sodium.number_input("Level of sodium in the blood (mEq/L)",step=1)


st.write("---------------------------------------------")

sex,smoking,time = st.columns(3)

sex = sex.radio("Sex",["Male","Female"])
sex = male_female_bool[sex]

smoking = smoking.radio("Do you smoke?",["Yes","No"])
smoking = yes_no_bool[smoking]

time=time.number_input("Follow up period",step=1)

st.write("---------------------------------------------")

    
data_instance=[age,anaemia,creatinine_phosphokinase,diabetes,
               ejection_fraction,high_blood_pressure,platelets,
               serum_creatinine,serum_sodium,sex,smoking,time]


st.write("#### Predict the chances of a death event")

prediction_converter = {0:"Less probability of death",1:"More probability of death"}

if st.button("Predict"):
    prediction=predict(data_instance)
    prediction=prediction_converter[prediction[0]]
    
    st.write(prediction)














