import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    univ_df = pd.read_csv('../data/University Students Monthly Expenses.csv')
    return univ_df

def handle_categorical_data(col_name):
    st.write("Total missing values: " +str(univ_df[col_name].isna().sum()))
    st.write("Unique values:")
    for val in univ_df[col_name].unique():
        st.write(val)
    st.write("Most frequent value: " +str(univ_df[col_name].mode()[0]))
    st.write("Replacing missing values with most frequent value from " +col_name+ " column")

def handle_continuous_data(col_name):
    st.write("Total missing values: " +str(univ_df[col_name].isna().sum()))
    st.write("Mean: " +str(univ_df[col_name].mean()))
    st.write("Median: " +str(univ_df[col_name].median())) 
    st.write("Mean is greater than median! The distribution is positively skewed")
    st.write("Choosing median imputation for Monthly_expenses_$ column since the distribution is positively skewed.")



# load the data
univ_df = load_data()


# Data cleaning and transformation
univ_df_clean = univ_df.copy()
# Replace NA values in Monthly_expenses_$ with median of the available Monthly_expenses_$ values
univ_df_clean['Monthly_expenses_$'] = univ_df_clean['Monthly_expenses_$'].fillna(univ_df_clean['Monthly_expenses_$'].median())
univ_df_clean['Monthly_Subscription'] = univ_df_clean['Monthly_Subscription'].fillna(univ_df_clean['Monthly_Subscription'].mode()[0])
univ_df_clean['Cosmetics_&_Self-care'] = univ_df_clean['Cosmetics_&_Self-care'].fillna(univ_df_clean['Cosmetics_&_Self-care'].mode()[0])
univ_df_clean['Drinks'] = univ_df_clean['Drinks'].fillna(univ_df_clean['Drinks'].mode()[0])
univ_df_clean['Transporting'] = univ_df_clean['Transporting'].fillna(univ_df_clean['Transporting'].mode()[0])
univ_df_clean['Part_time_job'] = univ_df_clean['Part_time_job'].fillna(univ_df_clean['Part_time_job'].mode()[0])
univ_df_clean['Living'] = univ_df_clean['Living'].fillna(univ_df_clean['Living'].mode()[0])
univ_df_clean['Study_year'] = univ_df_clean['Study_year'].fillna(univ_df_clean['Study_year'].mode()[0])



st.title('University Students Monthly Expenses')

# show the data in a table
if st.sidebar.checkbox('Show Original data'):
    st.header("Original Data")
    st.write(univ_df)

if st.sidebar.checkbox('Data cleaning strategies'):
    st.write("Total number of records in the dataframe: " + str(len(univ_df)))
    # ToDo: Add code to show Unique values per column, NA values per column and showcase data transformation strategies 
    selected_option = st.selectbox(
        "Choose a column to view data cleaning and transformations",
        ("Study_year","Living","Part_time_job","Transporting","Smoking","Drinks","Cosmetics_&_Self-care","Monthly_Subscription", "Monthly_expenses_$", "Home phone", "Mobile phone"),
    )

    if(selected_option == 'Monthly_expenses_$'):
        handle_continuous_data('Monthly_expenses_$')
    else:
        handle_categorical_data(selected_option)

if st.sidebar.checkbox('Show Cleaned data'):
    st.header("Cleaned data")
    st.write(univ_df_clean)



