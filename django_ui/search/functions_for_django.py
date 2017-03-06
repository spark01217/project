import pandas as pd
from .regression import predict


def fetch_current_data(neighborhood_code):
    res = {}

    datafile = 'data/current_data.csv'
    df = pd.read_csv(datafile)
    row = df[(df['community'] == neighborhood_code) & (df["date"] == 2016)]

    res['crime'] = int(row.iloc[0]['crime_freq'])
    res['school'] = int(row.iloc[0]['score'])
    res['income'] = int(row.iloc[0]['income'])
    res['price'] = int(row.iloc[0]['value'])

    if int(row.iloc[0]['cta']) == 1:
        res['cta'] = 'Yes'
    else:
        res['cta'] = 'No'

    return res


def fetch_new_price(alt_crime, alt_school, alt_income, alt_cta):
    price = predict(alt_crime, alt_income, alt_school, alt_cta)
    return price
