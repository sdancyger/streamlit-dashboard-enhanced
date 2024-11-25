import streamlit as st
import pandas as pd

# App title
st.title("Learning Modalities")

# Introduction text
st.write("""
In this dashboard, we will visualize data relating to school learning modalities.
""")

# Load the dataset
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000")

# data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# display dataset
st.metric("Rows", len(df))

# display top 5 rows
st.dataframe(df.head())
