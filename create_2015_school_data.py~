# Add school data for 2015 by averaging 2014/2016 data
#
# Something Creative


import csv


def create_data_list(filename):
    """
    Takes in csv file, creates a list of lists from the data.
    """

    with open(filename) as input_file:
        reader = csv.reader(input_file)
        data = []
        for row in reader:
            data.append(row[1:])

    data = data[1:]

    return data


def convert_data_structure(data):
    """
    Converts the dataset from a list of lists to a a list of dictionaries.
    """

    l_2012, l_2013, l_2014, l_2016 = [], [], [], []

    codes = []

    for row in data:

        year = row[0]
        score = int(row[1])
        name = row[2]
        code = int(row[3])
        codes.append(code)

        d = {'code': code, 'name': name, 'score': score}

        if year == '2012':
            l_2012.append(d)
        if year == '2013':
            l_2013.append(d)
        if year == '2014':
            l_2014.append(d)
        if year == '2016':
            l_2016.append(d)

    data_dict = {2012: l_2012, 2013: l_2013, 2014: l_2014, 2016: l_2016}

    codes = list(set(codes))

    return data_dict, codes


def aggregate_data(data_dict, codes):
    """
    Takes in the data dictionary and a list of codes. Aggregates the data so that each
    community only has one school_score.
    """

    data_agg = {}
    for year in data_dict:
        d = {}
        for code in codes:
            code_scores = []
            for row in data_dict[year]:
                if row['code'] == code:
                    code_scores.append(row['score'])
            avg_score =  int(sum(code_scores) / len(code_scores))
            d[code] = avg_score
            data_agg[year] = d

    return data_agg


def create_2015_data(data_agg, codes):

    data_2014 = data_agg[2014]
    data_2016 = data_agg[2016]
    data_2015 = {}

    for code in codes:
        data_2015[code] = int((data_2014[code] + data_2016[code]) / 2)

    return data_2015


def create_list_to_write(dataset, output_file):

    list_to_write = [['year', 'code', 'score']]

    for year in dataset:
        one_year_data = dataset[year]
        for key in one_year_data.keys():
            ROW = [str(year), str(key), str(one_year_data[key])]
            list_to_write.append(ROW)

    return list_to_write


def write_to_csv(dataset, filename):

    with open(filename, 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(dataset)


if __name__ == "__main__":

    input_file = 'final_data/school_data.csv'
    output_file = 'final_data/final_school_data.csv'

    data_list = create_data_list(input_file)

    data_dict, codes = convert_data_structure(data_list)

    data_agg = aggregate_data(data_dict, codes)

    data_agg[2015] = create_2015_data(data_agg, codes)

    list_to_write = create_list_to_write(data_agg, output_file)

    write_to_csv(list_to_write, output_file)
