import streamlit as st
import joblib
import pandas as pd


model=joblib.load("model/linear_model.pkl")
encoder=joblib.load("model/label_encoder.pkl")
scaler=joblib.load("model/scaler.pkl")

st.title("\tprediction model")

df=pd.read_csv(r"datasets\dfc.csv")

title = st.selectbox("Job Title", df['JobTitle'].unique())
if title:
    jobTitleEncode = encoder.transform([title])[0]
overtime=st.number_input("over time pay")
OtherPay=st.number_input("other pay")
Benefits=st.number_input("benefts")
totalpay=st.number_input("total pay")
year=st.number_input("year")
inty=int(year)
features = ['JobTitle', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'Year']
dic = {
    "JobTitle": [jobTitleEncode],
    "OvertimePay": [overtime],
    "Benefits": [Benefits],
    "OtherPay": [OtherPay],
    "TotalPay": [totalpay],
    "Year": [inty]
}
x=pd.DataFrame(dic,columns=features)
btn=st.button("predict")
if btn:
    st.write(f"your expected salary =  {round(model.predict(x)[0],2)}")