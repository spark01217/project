import csv
import pandas as pd
from math import isnan

data = pd.read_csv('Cleaned_Crimes.csv')
population = pd.read_csv("data/Community Area populations.csv", index_col = "Num")


data = data[['Community Area', 'FBI Code', 'Year']]

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

for i in range (2012, 2017):
	is_year = data["Year"] == i
	data_dict[i] = data[is_year]
	data_dict[i] = data_dict[i][pd.notnull(data_dict[i]["Community Area"])]
	data_dict[i] = data_dict[i][data_dict[i]["Community Area"] != 0.0]

def crime_frequency(dat, year):
	crime = {}
	for comarea in dat[year]["Community Area"].unique():
		crime[comarea] = {"Murder": 0, "Assault": 0, "Theft": 0, "Index": 0}
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
for i in range(2012, 2017):
	a = crime_frequency(data_dict, i)
	for j in range(1, 78):
		result.append(a[j]["Index"])
		year.append(i)
		neighbor.append(j)

final_list = pd.DataFrame({'Year': year, 'Index Crime Rate': result, 'community': neighbor}, index = neighbor)
final_list = final_list.pivot_table("Index Crime Rate", "community", "Year")
final_list.columns = ["2012_Crime", "2013_Crime", "2014_Crime", "2015_Crime", "2016_Crime"]
final_list.to_csv('final_crime_data.csv')
