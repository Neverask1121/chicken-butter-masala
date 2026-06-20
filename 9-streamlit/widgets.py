## To create more interactive applications

import streamlit as st

st.title("StramLit text input")

name=st.text_input("Enter your name")
if name:
  st.write(f"Hello, {name}")