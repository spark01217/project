import pandas as pd

df = pd.read_csv("../raw_file/income.csv")
# Leave only columns of interest
df = df.drop(df.columns[[1,2,3,4]], axis = 1)
df.columns = ["community", "2010", "2011", "2012"]
df = df[df['community'] == "Median household income"]

df = df.reset_index(drop=True)
l = list(range(1, 78))
df["community"] = pd.Series(l)
# Some hard-code fixes
df = df.drop(df.index[77])
df["2010"] = df["2010"].str.replace("$", "")
df["2011"] = df["2011"].str.replace("$", "")
df["2012"] = df["2012"].str.replace("$", "")
df["2010"] = df["2010"].str.replace(",", "")
df["2011"] = df["2011"].str.replace(",", "")
df["2012"] = df["2012"].str.replace(",", "")
df["2010"] = df["2010"].astype(int)
df["2011"] = df["2011"].astype(int)
df["2012"] = df["2012"].astype(int)
df["community"] = df["community"].astype(int)
e_2013 = []
e_2014 = []
e_2015 = []
e_2016 = []

# Linear extrapolation for income data
for i in range(len(df)):
	a = df['2011'][i] - df['2010'][i]
	b = df['2012'][i] - df['2011'][i]
	avg = (a+b)/2
	e_2013.append(df['2012'][i] + avg)
	e_2014.append(df['2012'][i] + 2*avg)
	e_2015.append(df['2012'][i] + 3*avg)
	e_2016.append(df['2012'][i] + 4*avg)

df['2013'] = pd.Series(e_2013).astype(int)
df['2014'] = pd.Series(e_2014).astype(int)
df['2015'] = pd.Series(e_2015).astype(int)
df['2016'] = pd.Series(e_2016).astype(int)

df = df.drop(df.columns[[1,2]], axis=1)
df = df.unstack()
df = df[77:]
df = df.to_frame()
df = pd.DataFrame(df.to_records())
df.columns = ["date", "community", "income"]
df["community"] += 1

df.to_csv('../django_ui/search/data/final_income_data.csv', index=False)

