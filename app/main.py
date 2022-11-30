import streamlit as st
import pandas as pd

@st.cache
def load_data():
    df = pd.read_csv('../data/University Students Monthly Expenses.csv')
    return df

st.title('University Students Monthly Expenses')

# load the data
df = load_data()

# show the data in a table
if st.sidebar.checkbox('Show dataframe'):
    st.write(df)