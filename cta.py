dta = pd.read_csv('/CTA_Ridership.csv')

dta = dta.sort(['date','rides'], axis = 0, ascending =[True, False])

# pd.dta.sort_values(['date', 'rides'], axis=0)
dta['date'] = pd.to_datetime(dta['date'])
dta = dta.groupby('date').head(10)
# dta = dta.groupby('date')['rides'].transform(sum)

# dta.to_csv('/home/zpzhu/cs122-win-17-zpzhu/pa3/ui/project/cta_data.csv')
def calctot(df):
    #delete columns
    df = df.drop(['station_id', 'stationname', 'date', 'daytype'], axis = 1)
    #append sum row, ignoring non-numeric column metrics
    return df.append(df.sum(numeric_only=True), ignore_index=True)

#groupby and reset index
nc =  dta.groupby('date').apply(calctot).reset_index()
#delete old index column
nc = nc.drop(['level_1'], axis=1)
#add new column onto the dataframe

# dta['rides1'] = pd.Series(nc, index = dta['date'])

#fill NaN to value tot
dta['date'] = dta['date'].fillna('tot')