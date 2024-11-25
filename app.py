import streamlit as st
import pandas as pd
import numpy as np

# Title- 2024 AHI 507 Streamlit Example
st.title('2024 AHI 507 Streamlit Example')
st.write('This dashboard displays interactive dataset features relating to School Learning Modalities')

# Load data - School Learning Modalities 
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000")

# Data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# Dataset metric
st.metric("Rows", len(df))

# Display the top 5 rows of the dataset
st.dataframe(df.head())

df['week'].value_counts()

## box to show how many rows and columns of data we have: 
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Number of unique districts/schools:", df['district_name'].nunique())

## exposing first 1k of NCES 20-21 data
st.dataframe(df)



table = pd.pivot_table(df, values='student_count', index=['week'],
                       columns=['learning_modality'], aggfunc="sum")

table = table.reset_index()
table.columns

## line chart by week 
st.bar_chart(
    table,
    x="week",
    y="Hybrid",
)

st.bar_chart(
    table,
    x="week",
    y="In Person",
)

st.bar_chart(
    table,
    x="week",
    y="Remote",
)

# Bar chart
st.markdown("### Learning Modalities by Week")
table = pd.pivot_table(df, values='student_count', index='week', columns='learning_modality', aggfunc='sum')
table = table.reset_index()

st.bar_chart(table.set_index('week')['Hybrid'])
st.bar_chart(table.set_index('week')['In Person'])
st.bar_chart(table.set_index('week')['Remote'])

# interactive slider
st.markdown("### Random Data Generator")
slider_value = st.slider('Select the number of random data points:', 10, 100, 50)
random_data = np.random.randn(slider_value)
st.write(f"Generated Data:", pd.DataFrame(random_data, columns=["Values"]))

# Line Chart
st.line_chart(random_data)

import streamlit as st
import numpy as np

# Title
st.title('Interactive Line Chart with Slider')

# Add slider
slider_value = st.slider('Select the number of random data points:', min_value=10, max_value=100, value=50)

# Generate random data based on slider
random_data = np.random.randn(slider_value)

# Display
st.line_chart(random_data)

# Histogram 
st.markdown("### Data Histogram")
fig, ax = plt.subplots()
ax.hist(random_data, bins=10, color="blue", edgecolor="pink")
st.pyplot(fig)

