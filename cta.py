import pandas as pd


dta = pd.read_csv('/home/zpzhu/cs122-win-17-zpzhu/pa3/ui/project/CTA_Ridership.csv')

date_sort = dta.sort('date')
# dta['date'] = dta.to_datetime(dta.Date)
# df.sort('Date')