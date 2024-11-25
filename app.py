import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    """
    <style>
        .css-1v3fvcr { /* Streamlit button background color */
            background-color: #FF1493; 
        }
        .st-bw { /* Streamlit text and title color */
            color: #FF1493;
        }
        .st-ae { /* Adjust text in sidebar or widgets */
            color: #FF1493;
        }
        .st-hg { /* Adjusting the header colors */
            color: #FF1493;
        }
    </style>
    """, 
    unsafe_allow_html=True
)
# Title Enhanced streamlit dashboard
st.title('Enhanced Streamlit Dashboard')
st.write('This dashboard displays interactive dataset features relating to School Learning Modalities')

# Load data - School Learning Modalities 
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000")

# Data cleaning
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

# Dataset metric
st.metric("Rows", len(df))

# Display the top 5 rows of the dataset
st.dataframe(df.head())

df['week'].value_counts()

## box to show how many rows and columns of data we have: 
col1, col2, col3 = st.columns(3)
col1.metric("Columns", df.shape[1]) 
col2.metric("Rows", len(df))
col3.metric("Number of unique districts/schools:", df['district_name'].nunique())

## exposing first 1k of NCES 20-21 data
st.dataframe(df)



table = pd.pivot_table(df, values='student_count', index=['week'],
                       columns=['learning_modality'], aggfunc="sum")

table = table.reset_index()
table.columns

## line chart by week 
st.bar_chart(
    table,
    x="week",
    y="Hybrid",
)

st.bar_chart(
    table,
    x="week",
    y="In Person",
)

st.bar_chart(
    table,
    x="week",
    y="Remote",
)

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

# Histogram 
st.markdown("### Data Histogram")
fig, ax = plt.subplots()
ax.hist(random_data, bins=10, color="blue", edgecolor="pink")
st.pyplot(fig)
