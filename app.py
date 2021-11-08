# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:02:51 2020

@author: vishal_kharde
"""
##libraries

import streamlit as st
from PIL import Image

##Title

st.title('Welcome to BMI Calculator')

##BMI Image

img=Image.open("bmi.jpg")
st.image(img, width=700)

# Set a flag

h_mode=0

#Weight

weight=st.number_input("Enter your weight (in kgs)")

#Height

status=st.radio("Select your height format:",("cms","meters","feet"))

if(status=="cms"):
    h_mode=0
    height=st.number_input("Centimeters")
elif(status=="meters"):
    h_mode=1
    height=st.number_input("Meters")
else:
    h_mode=2
    height=st.number_input("Feet")
  
## Calculate BMI 
    
if(st.button("Calculate BMI")):
    if(h_mode==0):
        bmi=weight/((height/100)**2)
        st.text(bmi)
    elif(h_mode==1):
        bmi=weight/(height**2)
        st.text(bmi)
    else:
             #1meter=3.28
        bmi=weight/(((height/3.28))**2)
        st.text(bmi) 
        
        
    if bmi<16:
        st.error("You are Extremely Underweight")
    elif bmi>= 16 and bmi<18.5:
        st.warning("You are Underweight")
    elif bmi>=18.5 and bmi<25:
        st.success("Healthy")
        st.balloons()
    elif bmi >= 25 and bmi < 30:
        st.warning("Overweight")
    elif bmi >= 30:
        st.error("Extremely Overweight")      
 
    

        
        
        
        
        
        
        
        
        
        
        
        
