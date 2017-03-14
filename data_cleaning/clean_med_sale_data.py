import openpyxl
import glob, os
import pandas as pd

# Using the glob library, I extracted all the names of the web-scraped files into
# a single list "excels."  
excel_names = glob.glob("../raw_file/med_sale_data/*.csv")
excels = []

# I concatenated all the files in the list "excels" into a single dataframe.
for name in sorted(excel_names):
   alt = pd.read_csv(name)
   alt["community"] = name[26:30]
   excels.append(alt)
combined = pd.concat(excels)

# I modify the name of a neighborhood that does not match the name of the
# neighborhood in the file of which columns are name of the neighborhood and
# neighborhood code numbers. 
id = pd.read_csv("id_name.csv")

# create dictionary that maps the names of neighborhoods to community codes
m = {}
for i in range(len(id)):
    m[id["id"][i]] = id["name"][i]

# Using the dictionary, I convert the community name into area code.
combined["community"] = combined["community"].astype(int)
combined["community"].replace(m, inplace=True)

map = pd.read_csv('Community Area populations.csv')
map["Community Area"] = map["Community Area"].str.strip()

m = {}
for i in range(len(map)):
    m[map["Community Area"][i].strip()] = map["Num"][i]

m["Canaryville"] = 61
m["Belmont Central"] = 19 
m["Cragin"] = 19
m["DePaul"] = 7
m["Goose Island"] = 8
m["Greektown"] = 28
m["Jeffrey Manor"] = 51 
m["Lakeview"] = 6
m["Pilsen"] = 31
m["Ravenswood"] = 4 
m["Roscoe Village"] = 5 
m["Sauganash"] = 8
m["Scottsdale"] = 70
m["Tri-Taylor"] = 28
m["Ukranian Village"] = 28 
m["University Village / Little Italy"] = 28
m["Washington Heights / Brainerd"] = 73
m["Bucktown"] = 22
m["Galewood"] = 25
m["Little Village"] = 30
m["Back of the Yards"] = 61
m["West Rogers Park"] = 2 
m["Wicker Park"] = 24

combined["community"].replace(m, inplace = True)

# Keep the observations if the date is between year 2012 to 2016,
# and convert year-month-day format to year format.
combined = combined[(combined["date"]>="2012-01-01") & (combined["date"]<"2017-01-01")]
combined["date"] = pd.to_datetime(combined["date"])
years = pd.Series([x.year for x in combined["date"]])
combined["date"] = years

# impute missing values with lagged values of the same community
combined.loc[204] = [2012, 58500, 54]
combined.loc[205] = [2013, 58500, 54]
combined.loc[206] = [2014, 52500, 54]
combined.loc[207] = [2015, 79000, 54]

# by year, compute the mean of the median home prices in communities
combined = combined.groupby(['date', 'community'])['value'].mean()
combined = combined.to_frame()
combined = pd.DataFrame(combined.to_records())
combined = combined.astype(int)
combined.to_csv("../django_ui/search/data/final_med_price_data.csv", index=False)
