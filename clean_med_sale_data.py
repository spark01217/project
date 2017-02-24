import openpyxl
import glob, os
import pandas as pd

# directory: project/med_sale_data
excel_names = glob.glob("*.csv")
excels = []
for name in sorted(excel_names):
   alt = pd.read_csv(name)
   alt["community"] = name[0:4]
   excels.append(alt)
combined = pd.concat(excels)

# directory: project
id = pd.read_csv("id_name.csv")
id.name[id.name=="Lake view"] = "Lake View"
m = {}
for i in range(len(id)):
    m[id["id"][i]] = id["name"][i]
combined["community"] = combined["community"].astype(int)
combined["community"].replace(m, inplace=True)

# directory: project/data
map = pd.read_csv('Community Area populations.csv')
for i in range(len(map)):
    m[map["Community Area"][i].strip()] = map["Num"][i]
combined["community"].replace(m, inplace = True)
combined = combined[combined["date"]>="2012-01-01"]
combined["date"] = pd.to_datetime(combined["date"])
years = pd.Series([x.year for x in combined["date"]])
combined["date"] = years
combined.groupby(['community', "date"]).mean().reset_index()
combined["value"] = combined["value"].astype(int)
combined = combined.sort_values(by="community")
combined = combined.reset_index(drop=True)
combined.to_csv("final_med_price_data.csv")
