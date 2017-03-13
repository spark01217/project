import csv
import pandas as pd
from math import isnan

# Crime data courtsey of City of Chicago databse
# Columns on FBI Code for each crime, year of crime, and area of crime
data = pd.read_csv("../raw_file/Crimes.csv")

# Importing community area population data for linear extrapolation
population = pd.read_csv("Community Area populations.csv", index_col = "Num")


data = data[['Community Area', 'FBI Code', 'Year']]

# Due to lack of census data for each specific year, used linear extrapolation
# to determine population by area for each year in 2012-2016
pop = {2012: [], 2013:[], 2014:[], 2015:[], 2016: []}
pop_2010 = list(population["2010"])
pop_diff = list(population["Difference"])
for i in range(len(pop_2010)):
	pop[2012].append(pop_2010[i] + (pop_diff[i]*2)/10)
	pop[2013].append(pop_2010[i] + (pop_diff[i]*3)/10)
	pop[2014].append(pop_2010[i] + (pop_diff[i]*4)/10)
	pop[2015].append(pop_2010[i] + (pop_diff[i]*5)/10)
	pop[2016].append(pop_2010[i] + (pop_diff[i]*6)/10)


data_dict= {}

# Clean data for any missing values and nulls
for i in range (2012, 2017):
	is_year = data["Year"] == i
	data_dict[i] = data[is_year]
	data_dict[i] = data_dict[i][pd.notnull(data_dict[i]["Community Area"])]
	data_dict[i] = data_dict[i][data_dict[i]["Community Area"] != 0.0]

def crime_frequency(dat, year):
	'''
	Takes data and year as input; returns crime, a dictionary that contains 
	index crime (crime designated as dangerous by FBI) frequency per 100,000 people
	for each area
	'''
	crime = {}
	# Nested dictionary to keep count per area
	for comarea in dat[year]["Community Area"].unique():
		crime[comarea] = {"Murder": 0, "Assault": 0, "Theft": 0, "Index": 0}
	# Necessary to turn these into list; if not, pandas dataframe columns for some reason
	# unnecesarily elongates runtime of code
	fbi = list(dat[year]["FBI Code"])
	com = list(dat[year]["Community Area"])
	for i in range(len(fbi)):
		if fbi[i] == "01A":
			area = int(com[i])
			crime[area]["Murder"] += (1/pop[year][area-1]) * 100000
			crime[area]["Index"] += (1/pop[year][area-1]) * 100000
		elif fbi[i] ==  "02" or fbi[i] == "04A" or fbi[i] == "04B" or fbi[i] == "08A":
			area = int(com[i])
			crime[area]["Assault"] += (1/pop[year][area-1]) * 100000
			crime[area]["Index"] += (1/pop[year][area-1]) * 100000
		elif fbi[i] ==  "03" or fbi[i] == "05" or fbi[i] == "06" or fbi[i] == "07":
			area = int(com[i])
			crime[area]["Theft"] += (1/pop[year][area-1]) * 100000
			crime[area]["Index"] += (1/pop[year][area-1]) * 100000
		elif fbi[i] == "09":
			area = int(com[i])
			crime[area]["Index"] += (1/pop[year][area-1]) * 100000
	return crime

result = []
year = [] 
neighbor = []
# Formatting
for i in range(2012, 2017):
	a = crime_frequency(data_dict, i)
	for j in range(1, 78):
		result.append(a[j]["Index"])
		year.append(i)
		neighbor.append(j)

final_list = pd.DataFrame({'date': year, 'crime_freq': result, 'community': neighbor}, index = neighbor)
final_list = final_list.sort_index(by=["date", "community"])
final_list.to_csv('../django_ui/search/data/final_crime_data.csv', index=False)