import streamlit as st
import pandas as pd
import numpy as np

# Title Enhanced streamlit dashboard
st.title('Enhanced Streamlit Dashboard')
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

# Histogram 
st.markdown("### Data Histogram")
fig, ax = plt.subplots()
ax.hist(random_data, bins=10, color="blue", edgecolor="pink")
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Change button background color */
        button[title="Run"] { 
            background-color: #FF1493; 
            color: white;
        }
        /* Change main text and title color */
        .stApp {
            color: #FF1493;
        }
        /* Change sidebar and widgets text color */
        .css-1v3fvcr {
            color: #FF1493;
        }
        /* Change header text color */
        h1, h2, h3, .st-bw {
            color: #FF1493;
        }
        /* Change background color of Streamlit app */
        .stApp {
            background-color: #f5f5f5;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title for the app
st.title('Enhanced Streamlit Dashboard')
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

## Box to show how many rows and columns of data we have: 
col1, col2, col3 = st.columns(3)
