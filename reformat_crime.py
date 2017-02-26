import pandas as pd

b = pd.read_csv('final_crime_data.csv')

final_crime = pd.DataFrame()

final_crime['community'] = b['Neighborhood'][0:77]

final_crime['2012_crime'] = list(b['Index Crime Rate'][0:77])
final_crime['2013_crime'] = list(b['Index Crime Rate'][77:154])
final_crime['2014_crime'] = list(b['Index Crime Rate'][154:231])
final_crime['2015_crime'] = list(b['Index Crime Rate'][231:308])
final_crime['2016_crime'] = list(b['Index Crime Rate'][308:385])

final_crime.to_csv('final_data/reformed_crime_data')