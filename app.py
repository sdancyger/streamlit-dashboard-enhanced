
import streamlit as st
import pandas as pd
import numpy as np

# Streamlit
st.title('Data Collected')
st.write('This dashboard displays clear visualizations & interactive widgets.')


data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})

# Bar chart
st.bar_chart(data.set_index('Category'))

# Slider Widget
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected: {slider_value}')




st.title("Data Collected Interactive Slider")
st.markdown("This dashboard includes interactive components, visualizations, & descriptive text.")

# Interactive slider
num = st.slider("Choose the number of data points", 10, 100, 50)

# Generate Random Data
data = np.random.randn(num)

# Display Data Table
st.write("Generated Data:", pd.DataFrame(data, columns=["Values"]))

# Line Chart
st.line_chart(data)


import streamlit as st
import numpy as np
