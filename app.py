import streamlit as st
import pandas as pd
import numpy as np

# Streamlit
st.title('Data Collected')
st.write('This dashboard displays clear visualizations & interactive widgets for AD Data')

st.text("""Focus on AD dataset.""")

# data set link https://data.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv/about_data

df = pd.read_csv("https://data.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv/about_data")

## data cleaning 
df['week_recoded'] = pd.to_datetime(df['week'])
df['zip_code'] = df['zip_code'].astype(str)

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


# Streamlit app layout
st.title("Districts by Learning Modality")

# Display all modalities in a dropdown
modalities = df["learning_modality"].unique()
selected_modality = st.selectbox("Select a Learning Modality:", modalities)

# Filter districts based on selected modality
filtered_df = df[df["learning_modality"] == selected_modality]

# Limit to top 20 districts
top_5_districts = filtered_df.head(20)

# Display filtered districts
st.subheader(f"20 Districts with Learning Modality: {selected_modality}")
st.write(top_5_districts["district_name"].tolist())


# Filter based on selected modality
filtered_data = df[df["learning_modality"] == selected_modality]


# Function to get the learning modality of a district
def get_learning_modality(district_name):
    """
    Returns the learning modality for a given district name.
    """
    result = df[df["district_name"] == district_name]
    if not result.empty:
        return result.iloc[0]["learning_modality"]
    else:
        return "District not found"

# Streamlit App Layout
st.title("Learning Modality Lookup")

# Input from user
district_input = st.text_input("Enter District Name:", "")

# Display the learning modality if a district is entered
if district_input:
    modality = get_learning_modality(district_input)
    st.write(f"The learning modality for **{district_input}** is: **{modality}**")
    