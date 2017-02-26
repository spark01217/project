import pandas as pd

crime = pd.read_csv('final_data/final_crime_data.csv')
income = pd.read_csv('final_data/final_income_data.csv')
cta = pd.read_csv('final_data/final_cta_data.csv')
school = pd.read_csv('final_data/final_school_data.csv')
price = pd.read_csv('final_data/final_med_price_data.csv')

merge = price.merge(crime, income, cta, school, on='community')
