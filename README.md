# Modeling Chicago Neighborhood Home Prices #
# with Socioeconomic Variables #
Winter 2017 <br />

Edward Hayes <br />
Sangwoo Park <br />
Jinsung Kim <br />
Zhipeng Zhu <br />

##Abstract##
Besides the characteristics of the dwelling unit itself, urban residential housing prices depend on neighborhood
characteristics such as crime rate, the median household income of the neighborhood, transportation accessibility,
quality of education and etc. This study estimates the impact of neighborhood characteristics on housing prices in
the city of Chicago. By using data of home prices and socioeconomic factors of neighborhoods from 2012 to 2016,
including median household income, average public school transcript score, crime rate and whether the neighborhood
has a CTA L station, panel regression using GLS was executed.

##Pulling up the Website##
Go into the django_ui directory, and then input <br />
```
python manage.py runserver
```
in the terminal. <br />
And then go to http://127.0.0.1:8000 in a browser.

##Website##
Our website displays <br />
1) Most recent (2016) median home price and values of socioeconomic factors for different neighborhoods <br />
2) Estimated median home price for an arbitrary neighborhood with user-input values of socioeconomic factors <br />

##Installation##
In order to run the codes for web scraping, data cleaning and pulling up the website,
Python Libraries including

- openpyxl
- django
- numpy
- pandas
- gdal-bin
- pyshp
- chicago_neighborhood_finder

In order to use the chicago_neighborhood_finder library, which converts a set of latitude and longitude (i.e. (92.3124, 41.3471))
into the name of Chicago neighborhood (i.e. West Englewood), first install the library gdal.
```
sudo apt-get install gdal-bin
```
then, install pyshp library, and finally the python requirements for the codes with 
```
sudo pip3 install pyshp
sudo pip3 install -r setup_library/requirements.txt
```

