import openpyxl
import pandas as pd
"""
sudo apt-get install gdal-bin
pip3 install --user -r requirements.txt
sudo pip3 install shapefile
sudo pip3 install pyshp
"""
run chicago_community_areas.py
areas = get_community_area_coords()
df = pd.read_csv('/data/school_quality.csv', header=None)
lng1 = df.loc[:,1][0:1880]
lng2 = df.loc[:,1][1880:] 
lat1 = df.loc[:,2][0:1880]
lat2 = df.loc[:,2][1880:]
df["lat"] = lat1.append(lng2)
df["lng"] = lng1.append(lat2)
df['neighborhood'] = df.apply(lambda col: get_neighborhood_for_point(col["lng"], col["lat"], areas), axis=1)
map = pd.read_csv('Community Area populations.csv')
map["Community Area"] = map["Community Area"].str.strip()
df.drop(df.columns[[1,2,3]], axis=1, inplace=True)

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

l = []
for i in df["neighborhood"]:
    l.append(m[i])
df["code"] = pd.Series(l) 
df.drop(df.columns[[2,3]], axis=1, inplace=True)
df.columns = ['year', 'school', 'community']
df.to_csv("school_data.csv")
