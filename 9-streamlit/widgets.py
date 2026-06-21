## To create more interactive applications


import pandas as pd
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

data = {
  "Name" : ["John", "Jane", "Aditya", "Aisha"],
  "Age" : [79, 67, 18, 13],
  "City" : ["New York", "New York", "Hyderabad", "Hyderabad"]
}

df = pd.DataFrame(data)
df.to_csv("sampleData.csv")
st.write(df)

uploaded_file=st.file_uploader("Choose a csv file", type = "csv")

if uploaded_file is not None:
  df=pd.read_csv(uploaded_file)
  st.write(df)