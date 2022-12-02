import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import numpy as np

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

@st.cache
def load_data(filepath):
    data_df = pd.read_csv(filepath)
    return data_df

def handle_categorical_data(col_name):
    st.warning("Total missing values in original dataset: " +str(univ_df[col_name].isna().sum()), icon="⚠️")
    unique_vals = ''
    for val in univ_df[col_name].unique():
        unique_vals = unique_vals + ' '+ str(val)
    st.text('Unique values: ' +unique_vals)
    st.info("Most frequent value: " +str(univ_df[col_name].mode()[0]), icon="ℹ️")
    st.success('Strategy: Replace missing value with most frequent value from ' +col_name+ ' column' , icon="✅")

def handle_continuous_data(col_name):
    st.warning("Total missing values in original dataset: " +str(univ_df[col_name].isna().sum()), icon="⚠️")
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
    #st.write(univ_df.isna().sum())

if st.sidebar.checkbox('Show Cleaned data'):
    st.header("Cleaned data")
    st.write(univ_df_clean)
    #st.write(univ_df_clean.isna().sum())

tab1, tab2, tab3 = st.tabs(["Data cleaning strategies", "Population per category", "Visualizations"])

with tab1:
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
    

with tab2:
    st.header("Data distribution")
    col1, col2 = st.columns(2)
    with col1:
        Gender_pop = univ_df_clean.groupby('Gender').size().reset_index(name='counts')
        donut_3 = alt.Chart(Gender_pop, title='Students belonging to each gender').mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="counts", type="quantitative"),
        color=alt.Color(field="Gender", type="nominal"),
        tooltip='counts:Q'
        )
        st.altair_chart(donut_3, use_container_width=True)
        study_year_pop = univ_df_clean.groupby('Study_year').size().reset_index(name='counts')
        donut_1 = alt.Chart(study_year_pop, title='Number of students in each study year').mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="counts", type="quantitative"),
        color=alt.Color(field="Study_year", type="nominal"),
        tooltip='counts:Q'
        )
        st.altair_chart(donut_1, use_container_width=True)

    with col2:
        Age_pop = univ_df_clean.groupby('Age').size().reset_index(name='counts')
        donut_4 = alt.Chart(Age_pop, title='Number of students belonging to each age group').mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="counts", type="quantitative"),
        color=alt.Color(field="Age", type="nominal"),
        tooltip='counts:Q'
        )
        st.altair_chart(donut_4, use_container_width=True)

        Living_pop = univ_df_clean.groupby('Living').size().reset_index(name='counts')
        donut_2 = alt.Chart(Living_pop, title='Number of students in each living arrangement').mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="counts", type="quantitative"),
        color=alt.Color(field="Living", type="nominal"),
        tooltip='counts:Q'
        )
        st.altair_chart(donut_2, use_container_width=True)

with tab3:
    # scatter_1 = alt.Chart(univ_df_clean).mark_circle(size=60).encode(
    # x='Age',
    # y='Monthly_expenses_$',
    # color='Gender',
    # tooltip=['Gender', 'Age', 'Monthly_expenses_$']).interactive()
    # st.altair_chart(scatter_1, use_container_width=True)

    st.title('Bar charts')

    age_vs_avg_monthly_income = univ_df_clean.groupby('Age')['Monthly_expenses_$'].mean().reset_index()
    bar_1= alt.Chart(age_vs_avg_monthly_income, title='Age Vs Average monthly expense in $').mark_bar().encode(
    x='Age:O',
    y=alt.Y('Monthly_expenses_$:Q', title='Average Monthly Expense($)'),
    color= alt.Color('Monthly_expenses_$:Q', legend=alt.Legend(title=None, orient="right")),
    tooltip='Monthly_expenses_$:Q')
    st.altair_chart(bar_1, use_container_width=True)

    st.title('Heat maps')

    heat_map_1 = alt.Chart(univ_df_clean, title='Impact of smoking on monthly expenses').mark_rect().encode(
    alt.X('Smoking:N'),
    alt.Y('Study_year:N'),
    alt.Color('Monthly_expenses_$:Q', scale=alt.Scale(scheme='greenblue')),
    tooltip='Monthly_expenses_$:Q')
    st.altair_chart(heat_map_1, use_container_width=True)

    heat_map_2 = alt.Chart(univ_df_clean, title='Impact of drinks on monthly expenses').mark_rect().encode(
    alt.X('Drinks:N'),
    alt.Y('Study_year:N'),
    alt.Color('Monthly_expenses_$:Q', scale=alt.Scale(scheme='greenblue')),
    tooltip='Monthly_expenses_$:Q')
    st.altair_chart(heat_map_2, use_container_width=True)

    heat_map_3 = alt.Chart(univ_df_clean, title='Impact of living situation on monthly expenses').mark_rect().encode(
    alt.X('Living:N'),
    alt.Y('Study_year:N'),
    alt.Color('Monthly_expenses_$:Q', scale=alt.Scale(scheme='greenblue')),
    tooltip='Monthly_expenses_$:Q')
    st.altair_chart(heat_map_3, use_container_width=True)

    

    
