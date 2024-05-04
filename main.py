import pypickle as py
import streamlit as st
from sklearn.linear_model import LogisticRegression
import numpy as np
st.title("Automotive Vehicle Engine Health")
st.header("By leveraging the measurements obtained from various sensors, technicians can input these data points and infer the condition or health status of an automotive engine")
model=py.load("lg.pkl")
#testing the model using logistic regression because it performed better than other models
user_input1=st.number_input('Engine rpm ')
user_input2=st.number_input('Lub oil pressure ')
user_input3=st.number_input('Fuel pressure ')
user_input4=st.number_input('Coolant pressure ')
user_input5=st.number_input('lub oil temp ')
user_input6=st.number_input('Coolant temp ')
predictionx=[[user_input1,user_input2,user_input3,user_input4,user_input5,user_input6]]
predictx = model.predict(predictionx)
if st.button("ENTER"):
  if predictx==1:
    st.success("Engine is good")
  else:
    st.warning("Engine is not good")