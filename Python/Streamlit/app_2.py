from json import load
import pandas as pd
import streamlit as st
import numpy as np 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("Flower Classification App")

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns = iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
X = df.drop('species', axis=1)
y = df['species']
model.fit(X, y)

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(X['sepal length (cm)'].min()), float(X['sepal length (cm)'].max()), float(X['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal Width", float(X['sepal width (cm)'].min()), float(X['sepal width (cm)'].max()), float(X['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal Length", float(X['petal length (cm)'].min()), float(X['petal length (cm)'].max()), float(X['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal Width", float(X['petal width (cm)'].min()), float(X['petal width (cm)'].max()), float(X['petal width (cm)'].mean()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

prediction = model.predict(input_data)
pred_spec = target_names[prediction][0]

st.write('Predictions')
st.write(f"The Flower is {pred_spec}")
