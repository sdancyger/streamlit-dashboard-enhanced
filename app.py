import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Streamlit App Title
st.header("Alzheimer's Disease and Healthy Aging Dashboard")
st.subheader("Exploring dataset data from 2024 Alzheimer's Disease and Healthy Aging.")

# Load the dataset (first 100 rows)
file_path = "/Users/sarahdancyger/Downloads/Alzheimer_s_Disease_and_Healthy_Aging_Data_20241124.csv"
df = pd.read_csv(file_path).head(100)


# Data preview
st.markdown("### Data Preview (First 100 Rows):")
st.dataframe(df)

# Data Cleaning (adjust columns as per the dataset you are using)
# Check for any necessary data type conversions or missing data handling
df['Year'] = pd.to_datetime(df['Year'], errors='coerce')  # Example: if there's a 'Year' column, make sure it's in datetime format
df['Age_Group'] = df['Age_Group'].astype(str)  # Example: ensure 'Age_Group' column is a string
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')  # Example: ensure numeric column 'Value'

# Show data metrics
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Number of unique Age Groups", df['Age_Group'].nunique())
