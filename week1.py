import streamlit as st
import pandas as pd

st.title("📊 Sales Data Visualization")

data = pd.read_csv("employees.csv")

st.subheader("📌 Available Columns")
st.write(list(data.columns))

st.subheader("👀 Data Preview")
st.dataframe(data.head())

if len(data.columns) >= 2:
    x_axis = st.selectbox("Select X-axis", data.columns)
    y_axis = st.selectbox("Select Y-axis", data.columns.drop(x_axis))

    chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart"])

    chart_data = data[[x_axis, y_axis]].dropna()
    chart_data = chart_data.set_index(x_axis)

    if chart_type == "Line Chart":
        st.line_chart(chart_data)
    else:
        st.bar_chart(chart_data)
else:
    st.warning("The CSV file must contain at least 2 columns.")







