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
st.metric("Columns", df.shape[1])
st.metric("Unique Districts", df['district_name'].nunique())

# display top 5 rows
st.dataframe(df.head())

# create pivot table  
pivot_table = pd.pivot_table(df, values='student_count', index='week', columns='learning_modality', aggfunc='sum')

# Plot charts
st.bar_chart(pivot_table["Hybrid"], use_container_width=True)
st.bar_chart(pivot_table["In Person"], use_container_width=True)
st.bar_chart(pivot_table["Remote"], use_container_width=True)

# Interactive modality
modality = st.selectbox("Select Learning Modality", df["learning_modality"].unique())
filtered_data = df[df["learning_modality"] == modality]

# Show top 5 districts
st.write(f"Top 5 Districts using {modality}:", filtered_data['district_name'].head().tolist())
