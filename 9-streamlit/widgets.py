## To create more interactive applications

import streamlit as st

st.title("StramLit text input")

name=st.text_input("Enter your name")

age=st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is something like this {age}")

options = ["Python", "Java", "CPP", "Javascript"]
choice = st.selectbox("Choose you favourite language", options)
st.write(f"Nigga selected: {choice}")

if name:
  st.write(f"Hello, {name}")