import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Enhanced Streamlit Dashboard")
st.markdown("This dashboard includes interactive components, visualizations, and descriptive text.")

# Interactive Slider
num = st.slider("Choose the number of data points", 10, 100, 50)

# Generate Random Data
data = np.random.randn(num)

# Display Data Table
st.write("Generated Data:", pd.DataFrame(data, columns=["Values"]))

# Line Chart
st.line_chart(data)

# Histogram
st.markdown("### Data Histogram")
fig, ax = plt.subplots()
ax.hist(data, bins=10, color="skyblue", edgecolor="black")
st.pyplot(fig)