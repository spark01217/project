import pandas as pd


dta = pd.read_csv('/home/student/project/CTA_Ridership.csv')

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
date_sort = dta.sort('date')

cid = pd.DataFrame('community code')

for i in range(len(date_sort)):
    cid.add(date_sort['stationname'].iloc(i))
    
# dta['date'] = dta.to_datetime(dta.Date)
# df.sort('Date')




name = {}

name['Austin-Forest Park'] = 0
name['Harlem-Lake'] = 0
name['Pulaski-Lake'] = 26
name['Quincy/Wells'] = 32
name['Davis'] = 0
name["Belmont-O'Hare"] = 21
name['Jackson/Dearborn'] = 32
name['Sheridan'] = 6
name['Damen-Brown'] = 04
name['Morse'] = 01
name['35th/Archer'] = 59
name['51st'] = 40
name['Skokie'] = 0
name['Pulaski-Cermak'] = 29
name['LaSalle/Van Buren'] = 32
name['Ashland-Lake'] = 28
name['Oak Park-Forest Park'] = 36
name['Sox-35th-Dan Ryan'] = 34
name['Randolph/Wabash'] = 32
name['Damen-Cermak'] = 0
name['Western-Forest Park'] = 32
name['Cumberland'] = 10
name['79th'] = 44
name['Kedzie-Homan-Forest Park'] = 27
name['State/Lake'] = 32
name['Main'] = 0
name['Central-Lake'] = 32
name['Ashland/63rd'] = 68
name['Indiana'] = 38
name['Western-Orange'] = 58
name['Division/Milwaukee'] = 24
name['Grand/State'] = 08
name['Berwyn'] = 77
name['UIC-Halsted'] = 28
name['Southport'] = 6
name['Washington/Dearborn'] = 32
name['Clark/Lake'] = 32
name['Forest Park'] = 0
name['Noyes'] = 0
name['Cicero-Cermak'] = 0
name['Clinton-Forest Park'] = 28
name['California-Cermak'] = 30
name['95th/Dan Ryan'] = 49
name['Merchandise Mart'] = 32
name['Racine'] = 28
name['Cicero-Lake'] = 25
name['Grand/Milwaukee'] = 24
name['Washington/State'] = 32
name['Garfield-South Elevated'] = 40
name['Foster'] = 0
name['Diversey'] = 07
name['Wilson'] = 03
name["Irving Park-O'Hare"] = 0
name['Jackson/State'] = 32
name['California/Milwaukee'] = 22
name['54th/Cermak'] =0
name['Damen/Milwaukee'] = 24
name['Kostner'] = 26
name['Ridgeland'] = 0
name['Clark/Division'] = 32
name['Madison/Wabash'] = 32
name['North/Clybourn'] = 08
name['Armitage'] = 07
name['Western/Milwaukee'] = 22
name['Adams/Wabash'] = 32
name['Laramie'] = 25
name['Chicago/Franklin'] = 08
name['East 63rd-Cottage Grove'] = 42
name['Washington/Wells'] = 32
name['Western-Cermak'] = 31
name["Harlem-O'Hare"] = 10 
name['Granville'] = 77
name['Lawrence'] = 03
name['Central Park'] = 29
name['Monroe/Dearborn'] = 32
name['Sedgwick'] = 08
name['Medical Center'] = 28
name['18th'] = 31
name['Library'] = 32
name['Francisco'] = 14
name['Thorndale'] = 77
name["O'Hare Airport"] = 76
name['Howard'] = 01
name['63rd-Dan Ryan'] = 68
name['Pulaski-Forest Park'] = 26
name['Midway Airport'] = 56
name['Halsted/63rd'] = 68 
name['Pulaski-Orange'] = 57
name['Cicero-Forest Park'] = 25
name['69th'] = 69
name['Cermak-Chinatown'] = 33
name['Rockwell'] = 04
name['Logan Square'] = 22
name['Polk'] = 28
name['Kedzie-Cermak'] = 29
name['Ashland-Orange'] = 31
name['Kedzie-Lake'] = 27
name['47th-South Elevated'] = 35
name['Monroe/State'] = 32
name['35-Bronzeville-IIT'] = 35
name['Halsted-Orange'] = 31
name['King Drive'] = 42
name['Kedzie-Midway'] = 63
name['Garfield-Dan Ryan'] = 37
name['Kedzie-Brown'] = 14
name['Jarvis'] = 01
name['Argyle'] = 03
name['Wellington'] = 06
name['Fullerton'] = 07
name['47th-Dan Ryan'] = 37
name["Addison-O'Hare"] = 16
name['43rd'] = 38
name['Jefferson Park'] = 11
name['Kimball'] = 14
name['Loyola'] = 01
name['Paulina'] = 06
name['Belmont-North Main'] = 06
name["Montrose-O'Hare"] = 14
name['LaSalle'] = 32
name['California-Lake'] = 27
name['Bryn Mawr'] = 77
name['Roosevelt'] = 33
name['Chicago/Milwaukee'] = 24
name['Addison-North Main'] = 06
name['87th'] = 44
name['Addison-Brown'] = 05
name['Chicago/State'] = 04
name['Irving Park-Brown'] = 05
name['Western-Brown'] = 04
name['Harrison'] = 32
name['Montrose-Brown'] = 04
name['Lake/State'] = 32
name['Conservatory'] = 27
name['Homan'] = 27
name['Morgan-Lake'] = 28
name['Cermak-McCormick Place'] =33
