# Run a scrape for the 5 year data on each
# neigborhood in Chicago
#
# Something Creative - CS122 Project

import util
import urllib.parse
import requests
import os
import bs4
import csv
import time

start_time = time.time()

def scrape_chart_data(html):
    '''
    Takes a html file for each neighborhood on Trulia.
    Extracts the data from a graph of median sale pricing
    using BeautifulSoup
    Inputs:
        html - the html doc
    Returns:
        data_points (list of dicts)
    '''
    request = util.get_request(html)
    doc = util.read_request(request)
    soup = bs4.BeautifulSoup(doc, 'lxml')

    scripts = soup.find_all('script')

    for script in scripts:
        if 'var CHART_DATA' in script.text:
            chart = script.text
            break

    start = 'medianSalesPoints: '
    end = 'salesVolumePoints'
    chart_list = (chart.split(start))[1].split(end)[0]
    chart_list = chart_list.replace('\n', '')
    chart_list = chart_list.replace('null', 'None')

    while chart_list[-1] == ' ':
        chart_list = chart_list[:-1]

    if chart_list[-1] == ',':
        chart_list = chart_list[:-1]

    data_by_bed_num = eval(chart_list)
    data_points = data_by_bed_num[-1]['points']

    return data_points


starting_url = 'https://www.trulia.com/home_prices/Illinois/Chicago-heat_map/city_by_neighborhood/ALP/nh/'

request = util.get_request(starting_url)
doc = util.read_request(request)
soup = bs4.BeautifulSoup(doc, 'lxml')

td1 = soup.find_all('tr', style='background-color: #FFFFFF;')
td2 = soup.find_all('tr', style='background-color: #EDEFF2;')
table_data = td1 + td2

name_to_link = {}
for neighborhood in table_data:
    td_tags = neighborhood.find_all('td')
    name = td_tags[0].find('a').text
    link = td_tags[0].find('a').get('href')
    if not link == '/real_estate/Chicago-Illinois/':
        name_to_link[name] = link

market_trends_pages = {}
id_name = []
for name in name_to_link.keys():
    url1 = 'https://www.trulia.com/'
    url2 = 'market-trends/'
    market_trends_page = url1 + name_to_link[name] + url2
    market_trends_pages[name] = market_trends_page

    trulia_id = name_to_link[name][-5:-1]
    d = {'name': name, 'id': trulia_id}
    id_name.append(d)

data = {}
for name in market_trends_pages.keys():
    link = market_trends_pages[name]
    data_points = scrape_chart_data(link)
    for node in data_points:
        node['value'] = int(node['value'])
    data[name] = data_points

for name in data.keys():
    trulia_id = name_to_link[name][-5:-1]
    filename = '../raw_file/med_sale_data/' + trulia_id + '_median_sale.csv'
    with open(filename, 'w') as output_file:
        fieldnames = ['date', 'value']
        # fieldnames = data[name][0].keys()
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data[name]:
            writer.writerow(row)

with open('../data_cleaning/id_name.csv', 'w') as output_file:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)

    writer.writeheader()
    for row in id_name:
        writer.writerow(row)

print("--- %s seconds ---" % (time.time() - start_time))
