import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data(filepath):
    data_df = pd.read_csv(filepath)
    return data_df

def handle_categorical_data(col_name):
    st.warning("Total missing values: " +str(univ_df[col_name].isna().sum()), icon="⚠️")
    unique_vals = ''
    for val in univ_df[col_name].unique():
        unique_vals = unique_vals + ' '+ str(val)
    st.text('Unique values: ' +unique_vals)
    st.info("Most frequent value: " +str(univ_df[col_name].mode()[0]), icon="ℹ️")
    st.success('Strategy: Replace missing value with most frequent value from ' +col_name+ ' column' , icon="✅")

def handle_continuous_data(col_name):
    st.warning("Total missing values: " +str(univ_df[col_name].isna().sum()), icon="⚠️")
    st.info("Mean: " +str(univ_df[col_name].mean()), icon="ℹ️")
    st.info("Median: " +str(univ_df[col_name].median()), icon="ℹ️") 
    st.text("Observation: Mean is greater than median! The distribution is positively skewed")
    st.success("Strategy: Use median imputation for Monthly_expenses_$ column since the distribution is positively skewed.", icon="✅")



# load the data
univ_df = load_data('../data/University Students Monthly Expenses.csv')
univ_df_clean = load_data('../data/univ_clean.csv')



st.title('University Students Monthly Expenses')

# show the data in a table
if st.sidebar.checkbox('Show Original data'):
    st.header("Original Data")
    st.write(univ_df)
    st.write(univ_df.isna().sum())

if st.sidebar.checkbox('Data cleaning strategies'):
    st.write("Total number of records in the dataframe: " + str(len(univ_df)))
    # ToDo: Add code to show Unique values per column, NA values per column and showcase data transformation strategies 
    selected_option = st.selectbox(
        "Choose a column to view data cleaning and transformations",
        ("Study_year","Living","Part_time_job","Transporting","Smoking","Drinks","Cosmetics_&_Self-care","Monthly_Subscription", "Monthly_expenses_$"),
    )

    if(selected_option == 'Monthly_expenses_$'):
        handle_continuous_data('Monthly_expenses_$')
    else:
        handle_categorical_data(selected_option)

if st.sidebar.checkbox('Show Cleaned data'):
    st.header("Cleaned data")
    st.write(univ_df_clean)
    st.write(univ_df_clean.isna().sum())



