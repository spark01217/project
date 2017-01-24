import csv


def open_data(file_name):
    exampleFile = open(file_name)
    example = csv.reader(exampleFile)
    exampleData = list(example)

    neighbor_list = []
    for neighbor in exampleData:
        neighbor_name = neighbor[1]
        neighbor_list.append(neighbor_name)
    neighbor_list.pop(0)
    return neighbor_list


list1 = open_data('census_data.csv')
list2 = open_data('trulia_scrape_data.csv')


commonName = set(list1)&set(list2)


input_file = open('census_data.csv', 'rb')
output_file = open('census_data_edit.csv', 'wb')
writer = csv.writer(output_file)
text1 = csv.reader(input_file)
text1_list = list(text1)
for row in text1_list:
    if row[1] in commonName:
        writer.writerow(row)
input_file.close()
output_file.close()

# with open('census_data.csv', 'rb') as csvfile:
#     text = csv.reader(csvfile)
#     for row in text:
#         print(row)

#         quotechar = '|',)
# file1 = csv.read()
# file2 = csv.read()