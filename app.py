import streamlit as st
import pandas as pd
import numpy as np

# Title and Introduction
st.title('Enhanced Streamlit Dashboard')
st.write('This dashboard showcases visualizations, interactive widgets, and data analysis.')

# Load the NCES School Learning Modalities dataset
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000")

# Data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# Display dataset metrics
st.metric("Rows", len(df))
st.metric("Columns", df.shape[1])
st.metric("Unique Districts", df['district_name'].nunique())

# Display the top 5 rows of the dataset
st.dataframe(df.head())

# Visualizing Learning Modalities Data (Bar Charts by week)
st.markdown("### Learning Modalities by Week")
table = pd.pivot_table(df, values='student_count', index='week', columns='learning_modality', aggfunc='sum')
table = table.reset_index()

st.bar_chart(table.set_index('week')['Hybrid'])
st.bar_chart(table.set_index('week')['In Person'])
st.bar_chart(table.set_index('week')['Remote'])

# Interactive Widget: Slider for generating random data
st.markdown("### Random Data Generator")
slider_value = st.slider('Select the number of random data points:', 10, 100, 50)
random_data = np.random.randn(slider_value)
st.write(f"Generated Data:", pd.DataFrame(random_data, columns=["Values"]))

# Line Chart for Random Data
st.line_chart(random_data)

# Histogram for Random Data
st.markdown("### Data Histogram")
fig, ax = plt.subplots()
ax.hist(random_data, bins=10, color="yellow", edgecolor="pink")
st.pyplot(fig)

# Dropdown to select learning modality and display top districts
st.markdown("### Districts by Learning Modality")
modality = st.selectbox("Select Learning Modality", df["learning_modality"].unique())
filtered_df = df[df["learning_modality"] == modality]

# Display top 5 districts for selected modality
top_districts = filtered_df['district_name'].head(5).tolist()
st.write(f"Top 5 districts with {modality} modality:", top_districts)

