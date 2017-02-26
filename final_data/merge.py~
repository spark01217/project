import pandas as pd

crime = pd.read_csv('reformed_crime_data.csv')
income = pd.read_csv('final_income_data.csv')
cta = pd.read_csv('binary_cta_data.csv')
school = pd.read_csv('final_school_data.csv')
price = pd.read_csv('final_med_price_data.csv')

merge = price.merge(crime, income, cta, school, on='community')