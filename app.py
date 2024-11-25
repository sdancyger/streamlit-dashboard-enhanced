pip install matplotlib
streamlit run app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit
st.title('Predict Hair Fall Data Dashboard')
st.write('This dashboard displays visualizations from the PredictHairFall dataset.')

# Load the dataset
file_path = "/Users/sarahdancyger/Downloads/PredictHairFall.csv"  # Update with the correct path
df = pd.read_csv(file_path)

# Show the dataset for reference
st.write("Dataset Preview:")
st.write(df.head())  # Display first few rows of the dataset

# Create a Bar Chart based on the dataset (replace with actual columns)
if 'Category' in df.columns and 'Values' in df.columns:
    # Create a Bar Chart with Yellow Bars and Pink Outlines
    fig, ax = plt.subplots()
    ax.bar(df['Category'], df['Values'], color='yellow', edgecolor='pink')

    # Set chart labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')
    ax.set_title('Bar Chart with Yellow Bars and Pink Outlines')

    # Display the custom bar chart in Streamlit
    st.pyplot(fig)
else:
    st.write("The dataset does not have 'Category' or 'Values' columns. Please check the column names.")

# Slider Widget for interactive feature
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected: {slider_value}')

# Interactive slider for number of data points
num = st.slider("Choose the number of data points", 10, 100, 50)

# Generate Random Data based on slider value (for testing)
random_data = np.random.randn(num)

# Display Data Table
st.write("Generated Data:", pd.DataFrame(random_data, columns=["Values"]))

# Line Chart based on the random data
st.line_chart(random_data)

# Optional Pie Chart using the data from the CSV
if 'Values' in df.columns:
    fig, ax = plt.subplots()
    ax.pie(df['Values'], labels=df['Category'], autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Display Pie Chart
    st.pyplot(fig)


