import streamlit as st
import pandas as pd
import numpy as np 

st.title('Streamlit Example')

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age:", 0, 100, 25)

options = ['Python','JavaScript','Java','C++']
select = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {select}")

st.checkbox("I agree to the terms and conditions")

st.write('This is a simple Streamlit app.')

df = pd.DataFrame({
    'col_1':[1,2,3,4,5],
    'col_2':[10,20,30,40,50]
})

st.write("Hare is the DataFrame:")
st.write(df)

# Creating a simple line chart

st.line_chart(df)