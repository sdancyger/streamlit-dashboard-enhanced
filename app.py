import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title Enhanced streamlit dashboard
st.title('Enhanced Streamlit Dashboard')
st.write('This dashboard displays interactive dataset features relating to School Learning Modalities')

# Load data - School Learning Modalities 
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000")

# Data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# Dataset metrics
st.metric("Rows", len(df))
st.metric("Columns", df.shape[1])
st.metric("Unique Districts", df['district_name'].nunique())

# Display the top 5 rows of the dataset
st.dataframe(df.head())

# Pivot table for learning modalities by week
st.markdown("### Learning Modalities by Week")
table = pd.pivot_table(df, values='student_count', index='week', columns='learning_modality', aggfunc='sum')
table = table.reset_index()

# Display the pivot table
st.write(table)

# Bar chart for each learning modality
st.markdown("### Bar Chart: Learning Modalities by Week")
st.bar_chart(table.set_index('week')['Hybrid'], use_container_width=True)
st.bar_chart(table.set_index('week')['In Person'], use_container_width=True)
st.bar_chart(table.set_index('week')['Remote'], use_container_width=True)

# Line chart for a selected number of random data points
st.markdown("### Random Data Line Chart")
slider_value = st.slider('Select the number of random data points:', 10, 100, 50)
random_data = np.random.randn(slider_value)
st.write(f"Generated Data:", pd.DataFrame(random_data, columns=["Values"]))
st.line_chart(random_data)
