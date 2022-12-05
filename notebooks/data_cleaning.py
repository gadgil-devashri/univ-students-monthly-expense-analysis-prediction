import pandas as pd

def load_data():
    univ_df = pd.read_csv('../data/University Students Monthly Expenses.csv')
    return univ_df

def clean_data():
    # Replace NA values in Monthly_expenses_$ with median of the available Monthly_expenses_$ values
    univ_df_clean['Monthly_expenses_$'] = univ_df_clean['Monthly_expenses_$'].fillna(univ_df_clean['Monthly_expenses_$'].median())
    univ_df_clean['Monthly_Subscription'] = univ_df_clean['Monthly_Subscription'].fillna(univ_df_clean['Monthly_Subscription'].mode()[0])
    univ_df_clean['Cosmetics_&_Self-care'] = univ_df_clean['Cosmetics_&_Self-care'].fillna(univ_df_clean['Cosmetics_&_Self-care'].mode()[0])
    univ_df_clean['Smoking'] = univ_df_clean['Smoking'].fillna(univ_df_clean['Smoking'].mode()[0])
    univ_df_clean['Drinks'] = univ_df_clean['Drinks'].fillna(univ_df_clean['Drinks'].mode()[0])
    univ_df_clean['Transporting'] = univ_df_clean['Transporting'].fillna(univ_df_clean['Transporting'].mode()[0])
    univ_df_clean['Part_time_job'] = univ_df_clean['Part_time_job'].fillna(univ_df_clean['Part_time_job'].mode()[0])
    univ_df_clean['Living'] = univ_df_clean['Living'].fillna(univ_df_clean['Living'].mode()[0])
    univ_df_clean['Study_year'] = univ_df_clean['Study_year'].fillna(univ_df_clean['Study_year'].mode()[0])

def write_data():
    univ_df_clean.to_csv('../data/univ_clean.csv', index=False)

# load the data
univ_df = load_data()
# Data cleaning and transformation
univ_df_clean = univ_df.copy()
# Clean Data
clean_data()
# Write clean data
write_data()