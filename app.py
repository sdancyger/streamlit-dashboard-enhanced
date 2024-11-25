import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Streamlit Title
st.title('Data Collected')
st.write('This dashboard displays clear visualizations & interactive widgets.')

# Example Data for Bar Chart
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})

# Bar chart
st.bar_chart(data.set_index('Category'))

# Slider Widget
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected: {slider_value}')

# Interactive Slider for Data Generation
st.title("Data Collected Interactive Slider")
st.markdown("This dashboard includes interactive components, visualizations, & descriptive text.")

# Interactive slider for generating random data points
num = st.slider("Choose the number of data points", 10, 100, 50)

# Generate Random Data
data = np.random.randn(num)

# Display Generated Data
st.write("Generated Data:", pd.DataFrame(data, columns=["Values"]))

# Line Chart for Random Data
st.line_chart(data)

# Pie Chart Section
st.title("Pie Chart Visualization")
st.markdown("This is a pie chart showing the distribution of categories.")

# Example Data for Pie Chart
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})

# Creating the pie chart
fig, ax = plt.subplots()
ax.pie(df['Values'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Display the pie chart
st.pyplot(fig)
