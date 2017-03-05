import openpyxl
import pandas as pd
"""
The geocoding library cannot be installed in CSIL desktops.
Please install them via your VM.

sudo apt-get install gdal-bin (VM)
sudo pip3 install -r setup_library/requirements.txt (VM)
sudo pip3 install pyshp (VM)

The installation will fail if you don't keep the installation order.
"""
run chicago_community_areas.py
areas = get_community_area_coords()

df = pd.read_csv('school_quality.csv', header=None)

lng1 = df.loc[:,1][0:1218]
lng2 = df.loc[:,1][1218:] 
lat1 = df.loc[:,2][0:1218]
lat2 = df.loc[:,2][1218:]
df["lat"] = lat1.append(lng2)
df["lng"] = lng1.append(lat2)
df['community'] = df.apply(lambda col: get_neighborhood_for_point(col["lng"], col["lat"], areas), axis=1)

map = pd.read_csv('Community Area populations.csv')
map["Community Area"] = map["Community Area"].str.strip()
df.drop(df.columns[[1,2,3,5,6]], axis=1, inplace=True)

m = {}
for i in range(len(map)):
    m[map["Community Area"][i].strip()] = map["Num"][i]

m["Garfield Park"] = 27
m["Bucktown"] = 22
m["West Loop"] = 32
m["United Center"] = 28
m["Little Italy, UIC"] = 28
m["Mckinley Park"] = 59
m["Grand Crossing"] = 69
m["Andersonville"] = 77
m["Little Village"] = 30
m["River North"] = 8
m["Ukrainian Village"] = 24
m["Printers Row"] = 32
m["East Village"] = 24
m["Wicker Park"] = 24
m["Sauganash,Forest Glen"] = 12
m["Old Town"] = 8
m["Chinatown"] = 32
m["Galewood"] = 25
m["Sheffield & DePaul"] = 7
m["Boystown"] = 6
m["Rush & Division"] = 8

df["community"].replace(m, inplace=True)
df.columns = ['date', 'score', 'community']
df = df.pivot_table("score", "community", "date")
df[2015] = (df[2014]+df[2016])/2
df.loc[26] = [54, 52, 60, 57, 58]
df.loc[67] = [42, 39, 54, 51, 53]
df = df.unstack(level=0)
df = df.to_frame()
df = pd.DataFrame(df.to_records())
df = df.astype(int)
df = df.rename(columns={'0': 'score'})
df = df.sort_index(by=["date", "community"])
df.to_csv("../final_data/final_school_data.csv", index=False)
