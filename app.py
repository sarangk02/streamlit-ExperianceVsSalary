# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt 
from sklearn.linear_model import LinearRegression


# ML Stuff
data = pd.read_csv("Salary_Data.csv")
x = np.array(data['YearsExperience']).reshape(-1,1)
y = np.array(data['Salary']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,y)


# Basic Setup of Page
st.title("Experiance based Salary")
nav = st.sidebar.radio('Navigate',["Home","Prediction","Contribute"])
st.image('hero.jpg')


# Individual Tabs
if nav == "Home":
    if st.checkbox("Show data"):
        st.table(data)

    graph = st.selectbox("What kind of Graph ?",["Non-Interactive","Interactive"])
    val = st.slider("Filter data using years",0,12)
    data = data.loc[data["YearsExperience"]>=val]
    
    if graph == "Non-Interactive":
        fig, ax= plt.subplots(figsize=(12,6))
        ax.scatter(data = data, x = 'YearsExperience', y = 'Salary')
        ax.set(xlabel = "Experiance", ylabel = "Salary")
        st.pyplot(fig)
    elif  graph=="Interactive" :
        altgraph = alt.Chart(data).mark_circle().encode(x = 'YearsExperience', y = 'Salary', tooltip = ['YearsExperience','Salary'])    
        st.altair_chart(altgraph, use_container_width=True)

elif nav == "Prediction":
    st.header("Prediction of Salary")
    yr = st.number_input("Enter Years of Experiance", min_value=0.00,max_value=15.00)
    yr1 = np.array(yr).reshape(-1,1)
    salary = round(lr.predict(yr1)[0][0], 2)

    
    if st.button("Predict"):
        st.success(f"Predicted Salary based on experiance of {yr} years is {salary}")
    
else :
    st.header("Contribute to our dataset")
    exp = st.number_input("Enter Your Experiance",0.0,20.0)
    sal = st.number_input("Enter Your Salary",0.00,500000.00,step = 1000.00)
    
    if st.button("Submit"):
        to_add = pd.DataFrame({
            "YearsExperience" : exp,
            "Salary" : sal
            },index = [0])
        to_add.to_csv("Salary_Data.csv",mode = 'a', header = False,index = False)
        st.success(f"Data => Experiance : {exp} and Salary => {sal} is Submitted")
    
