import streamlit as st
import pandas as pd


st.header("2024 AHI 507 Streamlit Example")
st.subheader("We are going to go through a couple different examples of loading and visualization information into this dashboard")

st.text("""In this streamlit dashboard, we are going to focus on some recently released school learning modalities data from the NCES, for the years of 2021.""")

# ## https://healthdata.gov/National/School-Learning-Modalities-2020-2021/a8v3-a3m3/about_data
df = pd.read_csv("https://healthdata.gov/resource/a8v3-a3m3.csv?$limit=50000") ## first 1k 

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
    