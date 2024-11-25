
import streamlit as st
import pandas as pd
import numpy as np

# Streamlit
st.title('Enhanced Streamlit Dashboard')
st.write('This dashboard showcases visualizations and interactive widgets.')


data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})

# Bar chart
st.bar_chart(data.set_index('Category'))

# Slider Widget
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'You selected: {slider_value}')




st.title("Enhanced Streamlit Dashboard")
st.markdown("This dashboard includes interactive components, visualizations, and descriptive text.")

# Interactive slider
num = st.slider("Choose the number of data points", 10, 100, 50)

# Generate Random Data
data = np.random.randn(num)

# Display Data Table
st.write("Generated Data:", pd.DataFrame(data, columns=["Values"]))

# Line Chart
st.line_chart(data)

import matplotlib.pyplot as plt


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Enhanced Streamlit Dashboard")

# Generate Random Data
data = np.random.randn(100)  # 100 random numbers

# Create Histogram
st.markdown("### Data Histogram")
fig, ax = plt.subplots()
ax.hist(data, bins=10, color="yellow", edgecolor="pink")
ax.set_title("Histogram of Random Data")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
st.pyplot(fig)


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Streamlit Dashboard with Checkboxes")

# Generate Random Data
data = np.random.randn(100)

# Checkbox - data table
if st.checkbox("Show Data Table"):
    st.write("Here is the generated data:", pd.DataFrame(data, columns=["Values"]))

# Checkbox -line chart
if st.checkbox("Show Line Chart"):
    st.markdown("### Line Chart")
    st.line_chart(data)

