import streamlit as st
import joblib
import pandas as pd

st.title("welcom to Sf Salary project")

st.write("One way to understand how a city government works is by looking at who it employs and how its employees are compensated. This data contains the names, job title, and compensation for San Francisco city employees on an annual basis from 2011 to 2014.")
st.subheader("Exploration Ideas")
st.write("""
1- How have salaries changed over time between different groups of people?\n
2- How are base pay, overtime pay, and benefits allocated between different groups?\n
3- Is there any evidence of pay discrimination based on gender in this dataset?\n
4- How is budget allocated based on different groups and responsibilities?
""")
st.image("dataset-cover.jpeg")