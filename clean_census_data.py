import openpyxl
import pandas as pd
df = pd.read_csv("census_data.csv")
df = df.drop(df.columns[[1]], axis=1)
df.columns = ['community', 'crowded', 'poverty', 'unemployment', 'no_diploma', 'nonworking', 'income', 'hardship']
df.to_csv("final_census_data.csv")
