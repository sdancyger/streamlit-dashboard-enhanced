import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit Header
st.title('Data Collected')
st.write('This dashboard displays clear visualizations & interactive widgets.')

# Load the dataset from Downloads (first 100 rows)
file_path = "/Users/sarahdancyger/Downloads/Alzheimer_s_Disease_and_Healthy_Aging_Data_20241124.csv"
df = pd.read_csv(file_path).head(100)

# Display the first few rows of the dataset
st.subheader("Dataset Overview")
st.write(df)

# Bar Chart example (with new data)
st.subheader("Bar Chart of the Data")
st.bar_chart(df['student_count'].head(10))  # Example using 'student_count' column, adjust based on actual data

# Slider Widget
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected: {slider_value}')

# Interactive Slider example
st.title("Data Collected Interactive Slider")
st.markdown("This dashboard includes interactive components, visualizations, & descriptive text.")

# Interactive slider to select number of data points
num = st.slider("Choose the number of data points", 10, 100, 50)

# Generate random data to use for visualization
random_data = np.random.randn(num)

# Display the generated data as a table
st.write("Generated Data:", pd.DataFrame(random_data, columns=["Values"]))

# Line Chart of generated data
st.line_chart(random_data)

# Pie chart of example dataset (modify as needed based on actual columns in your dataset)
st.subheader("Pie Chart of Data")
fig, ax = plt.subplots()
ax.pie(df['student_count'].head(4), labels=df['week'].head(4), autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
st.pyplot(fig)

# Display data filtered based on a week using a slider
min_date = pd.to_datetime(df['week_recoded']).min().date()
max_date = pd.to_datetime(df['week_recoded']).max().date()

# Slider to select week
selected_date = st.slider(
    "Select a week to filter the data:",
    min_value=min_date,
    max_value=max_date,
    value=min_date,
    format="YYYY-MM-DD"
)

# Filter data based on selected date
filtered_data = df[df['week_recoded'].dt.date == selected_date]

# Display filtered data and total student count by learning modality for the selected week
st.markdown(f"### Data for the selected week: {selected_date}")
if not filtered_data.empty:
    st.dataframe(filtered_data)

    modality_counts = filtered_data.groupby('learning_modality')['student_count'].sum().reset_index()
    modality_counts.columns = ['Learning Modality', 'Student Count']
    
    # Bar chart for the filtered data
    st.markdown("### Total Students by Learning Modality")
    st.bar_chart(modality_counts.set_index('Learning Modality'))
else:
    st.write("No data available for the selected week.")
