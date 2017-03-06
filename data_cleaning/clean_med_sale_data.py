import openpyxl
import glob, os
import pandas as pd

excel_names = glob.glob("../raw_file/med_sale_data/*.csv")
excels = []
for name in sorted(excel_names):
   alt = pd.read_csv(name)
   alt["community"] = name[14:18]
   excels.append(alt)
combined = pd.concat(excels)

id = pd.read_csv("id_name.csv")
id.name[id.name=="Lake view"] = "Lake View"
m = {}
for i in range(len(id)):
    m[id["id"][i]] = id["name"][i]
combined["community"] = combined["community"].astype(int)
combined["community"].replace(m, inplace=True)

map = pd.read_csv('data/Community Area populations.csv')
for i in range(len(map)):
    m[map["Community Area"][i].strip()] = map["Num"][i]
combined["community"].replace(m, inplace = True)
combined = combined[(combined["date"]>="2012-01-01") & (combined["date"]<"2017-01-01")]
combined["date"] = pd.to_datetime(combined["date"])
years = pd.Series([x.year for x in combined["date"]])
combined["date"] = years
combined.loc[204] = [2012, 58500, 54]
combined.loc[205] = [2013, 58500, 54]
combined.loc[206] = [2014, 52500, 54]
combined.loc[207] = [2015, 79000, 54]

combined = combined.groupby(['date', 'community'])['value'].mean()
combined = combined.to_frame()
combined = pd.DataFrame(combined.to_records())
combined = combined.astype(int)
combined.to_csv("../django_ui/search/data/final_med_price_data.csv", index=False)
