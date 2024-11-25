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

# Dataset metrics
st.metric("Rows", len(df))
st.metric("Columns", df.shape[1])
st.metric("Unique Districts", df['district_name'].nunique())

# Display the top 5 rows of the dataset
st.dataframe(df.head())

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
plt.plot(random_data, color="purple")
st.pyplot(plt)

# Histogram 
st.markdown("### Data Histogram")
fig, ax = plt.subplots(figsize=(10, 6))
table.plot(kind="bar", x="week", y=["Hybrid", "In Person", "Remote"], ax=ax, color=["red", "blue", "green"])
ax.set_xlabel("Week")
ax.set_ylabel("Student Count")
st.pyplot(fig)

# Dropdown to select learning modality + top districts
st.markdown("### Districts by Learning Modality")
modality = st.selectbox("Select Learning Modality", df["learning_modality"].unique())
filtered_df = df[df["learning_modality"] == modality]

# Display top 5 districts for selected modality
top_districts = filtered_df['district_name'].head(5).tolist()
st.write(f"Top 5 districts with {modality} modality:", top_districts)

