import pandas as pd
import functools
import pandas.stats.plm as plm

crime = pd.read_csv('final_data/final_crime_data.csv')
income = pd.read_csv('final_data/final_income_data.csv')
cta = pd.read_csv('final_data/final_cta_data.csv')
school = pd.read_csv('final_data/final_school_data.csv')
price = pd.read_csv('final_data/final_med_price_data.csv')

dfs = [crime, income, school, price]
df_final = functools.reduce(lambda left,right: pd.merge(left,right,on=["date", "community"]), dfs)
df_final = df_final.sort(["community", "date"])

cta_dict = cta.set_index("community").T.to_dict(orient="index")["cta"]
df_final["cta"] = df_final["community"].replace(cta_dict, inplace=False)
df_final["interaction"] = df_final["score"]*df_final["income"]

df_final = df_final.set_index(["community", "date"])
dfPanel = df_final.to_panel()

plm.PanelOLS(y = dfPanel['value'], x=dfPanel[['crime_freq', 'income', 'score', 'cta', 'interaction']],
            intercept= True, time_effects=False, dropped_dummies=True, verbose=True)

