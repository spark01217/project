import pandas as pd
df = pd.read_csv("income.csv")
df = df.drop(df.columns[[1,2,3,4]], axis = 1)
df.columns = ["community", "2010", "2011", "2012"]
df = df[df['community'] == "Median household income"]
df = df.reset_index(drop=True)
l = list(range(1, 78))
df["community"] = pd.Series(l)
df = df.drop(df.index[77])
df["2012"] = df["2010"].str.replace("$", "")
df["2012"] = df["2011"].str.replace("$", "")
df["2012"] = df["2012"].str.replace("$", "")
df["2012"] = df["2010"].str.replace(",", "")
df["2012"] = df["2011"].str.replace(",", "")
df["2012"] = df["2012"].str.replace(",", "")
df["2010"] = df["2010"].astype(int)
df["2011"] = df["2011"].astype(int)
df["2012"] = df["2012"].astype(int)
df["community"] = df["community"].astype(int)
df.to_csv("cleaned_income_data.csv")

