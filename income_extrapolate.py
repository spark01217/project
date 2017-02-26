import pandas as pd

dat = pd.read_csv('cleaned_income_data.csv')

dat = dat[['community', '2010', '2011', '2012']]


e_2013 = []
e_2014 = []
e_2015 = []
e_2016 = []

for i in range(len(dat)):
	a = dat['2011'][i] - dat['2010'][i]
	b = dat['2012'][i] - dat['2011'][i]
	avg = (a+b)/2
	e_2013.append(dat['2012'][i] + avg)
	e_2014.append(dat['2012'][i] + 2*avg)
	e_2015.append(dat['2012'][i] + 3*avg)
	e_2016.append(dat['2012'][i] + 4*avg)

dat['2013'] = e_2013
dat['2014'] = e_2014
dat['2015'] = e_2015
dat['2016'] = e_2016


dat = dat[['community', '2012', '2013', '2014', '2015', '2016']]

dat.columns = ['community', '2012_Income', '2013_Income', '2014_Income', '2015_Income', '2016_Income']

dat.to_csv('final_data/final_income_data.csv')
