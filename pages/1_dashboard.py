import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="dashboard",layout="wide")

st.title("SF Dashboard")
@st.cache_data
def read():
    return pd.read_csv("datasets/DFD.csv")
df=read()
button= st.button("show sample")
if button:
    st.dataframe(df.sample(5),use_container_width=True)


col1,col2=st.columns(2)
with col1:
   
    st.subheader("departments mean salariy", divider="gray")
    departmentg=df.groupby('department')['TotalPay'].mean().reset_index()
    st.bar_chart(data=departmentg,x="department",y="TotalPay",color="department",horizontal=True,height=400)


    st.subheader("top paid jobs", divider="gray")
    group=df.groupby('JobTitle')['TotalPay'].max().sort_values(ascending=False).head(5).reset_index()
    st.bar_chart(data=group,x="JobTitle",y="TotalPay",color="JobTitle",horizontal=True,height=400)

    st.subheader("top paid employees", divider="gray")
    group=df.groupby('EmployeeName')['TotalPay'].max().sort_values(ascending=False).head(5).reset_index()
    st.bar_chart(data=group,x="EmployeeName",y="TotalPay",color="EmployeeName",horizontal=True,height=400)

    st.subheader("most common jobs", divider="gray")
    most=df['JobTitle'].value_counts().head(5).reset_index()
    st.bar_chart(data=most,x="JobTitle",y="count",color="JobTitle",x_label="most common jobs",height=400)

    st.subheader("Years Totalpay", divider="gray")
    gg=df.groupby('Year')['TotalPay'].mean().reset_index()
    fig=px.pie(gg,names='Year',values="TotalPay",hole=0.4)
    st.plotly_chart(fig)
    #st.dataframe(group)
with col2:
    st.subheader("depatments count", divider="gray")
    group=df['department'].value_counts().head(5).reset_index()
    fig=px.pie(group,names='department',values="count",hole=0.4)
    st.plotly_chart(fig)

    st.subheader("least paid jobs", divider="gray")
    group=df.groupby('JobTitle')['TotalPay'].min().sort_values(ascending=False).tail(5).reset_index()
    st.bar_chart(data=group,x="JobTitle",y="TotalPay",color="JobTitle",horizontal=True,height=400)


    st.subheader("least paid employees", divider="gray")
    group=df.groupby('EmployeeName')['TotalPay'].min().sort_values(ascending=False).tail(5).reset_index()
    st.bar_chart(data=group,x="EmployeeName",y="TotalPay",color="EmployeeName",horizontal=True,height=400)

    st.subheader("least common jobs", divider="gray")
    most=df['JobTitle'].value_counts().tail(5).reset_index()
    st.bar_chart(data=most,x="JobTitle",y="count",color="JobTitle",x_label="most common jobs",height=400)

    st.subheader("Salary Vs Year", divider="gray")
    gg=df.groupby('Year')['TotalPay'].mean().reset_index()
    fig=px.line(gg,x='Year',y="TotalPay",markers=True,color=None,text="TotalPay",height=400)
    st.plotly_chart(fig)


st.subheader("Top Paid Jobs", divider="gray")
group = df.loc[df.groupby('JobTitle')['TotalPay'].idxmax()]
group = group.sort_values('TotalPay', ascending=False).head(10)
fig = px.bar(group, x="JobTitle", y="TotalPay", color="Year", height=600,width=600)
st.plotly_chart(fig)