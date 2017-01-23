# Scrape data from Trulia

import util
import urllib.parse
import requests
import os
import bs4
import csv

url = 'https://www.trulia.com/home_prices/Illinois/Chicago-heat_map/city_by_neighborhood/ALP/nh/'

request = util.get_request(url)
doc = util.read_request(request)
soup = bs4.BeautifulSoup(doc, 'lxml')

td1 = soup.find_all('tr', style='background-color: #FFFFFF;')
td2 = soup.find_all('tr', style='background-color: #EDEFF2;')
table_data = td1 + td2

t = {}

for neighborhood in table_data:
    td_tags = neighborhood.find_all('td')

    name = td_tags[0].find('a').text
    avg_listing = td_tags[1].text
    avg_sale = td_tags[3].text
    median_sale = td_tags[5].text
    price_per_sqft = td_tags[7].text
    trulia_popularity = td_tags[9].text

    tr = {  'Neighborhood': name,
            'Average Listing Price': avg_listing,
            'Average Sale Price': avg_sale,
            'Median Sale Price': median_sale,
            'Price Per Sqft': price_per_sqft,
            'Trulia Popularity': trulia_popularity,
            }

    tr = { name: [avg_listing, avg_sale, median_sale,
                    price_per_sqft, trulia_popularity]}
    t.update(tr)



    # csv_line = (
    #     name + ',' +
    #     avg_listing + ',' +
    #     avg_sale + ',' +
    #     median_sale + ',' +
    #     price_per_sqft + ',' +
    #     trulia_popularity + '\n'
    #     )
    #
    # csv_full += csv_line
