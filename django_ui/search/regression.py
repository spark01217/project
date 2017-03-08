import pandas as pd
import functools
import pandas.stats.plm as plm

crime = pd.read_csv('search/data/final_crime_data.csv')
income = pd.read_csv('search/data/final_income_data.csv')
cta = pd.read_csv('search/data/final_cta_data.csv')
school = pd.read_csv('search/data/final_school_data.csv')
price = pd.read_csv('search/data/final_med_price_data.csv')

dfs = [crime, income, school, price]
df_final = functools.reduce(lambda left, right: pd.merge(left,right,on=["date", "community"]), dfs)
df_final = df_final.sort(["community", "date"])

cta_dict = cta.set_index("community").T.to_dict(orient="index")["cta"]
df_final["cta"] = df_final["community"].replace(cta_dict, inplace=False)
df_final["interaction"] = df_final["score"]*df_final["income"]

df_final = df_final.set_index(["community", "date"])
dfPanel = df_final.to_panel()

model = plm.PanelOLS(y=dfPanel['value'], x=dfPanel[['crime_freq', 'income', 'score', 'cta', 'interaction']],
                     intercept=False, time_effects=False, dropped_dummies=True, verbose=True)


def predict(crime, income, school, cta):
    if cta != 0 and cta != 1:
        print("type cta: 0 for no cta station, or type cta: 1 for having a cta station.")
    elif school < 0 or school > 100:
        print("type school score between 0 and 100")
    elif crime < 0:
        print("crime rate must be positive")
    elif income < 0:
        print("median income must be positive")
    else:
        prediction = model.beta[0]*crime + model.beta[1]*income + model.beta[2]*school + model.beta[3]*cta + model.beta[4]*income*school
        if prediction < 0:
            prediction = 0

        return prediction


def fetch_current_data(neighborhood_code):
    res = {}

    datafile = 'search/data/current_data.csv'
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

