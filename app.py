
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
