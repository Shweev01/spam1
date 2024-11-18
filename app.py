import streamlit as st
import pickle

model=pickle.load(open('spam.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

st.title("Email Spam Classification Application")
st.write("This is a Machine Learning application to classify emails as spam or ham.")
st.title("Email Spam Classification Application")
st.write("This is a Machine Learning application to classify emails as spam or ham.")