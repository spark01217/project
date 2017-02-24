import csv

def create_data_list(filename):
    with open(filename) as input_file:

        reader = csv.reader(input_file)
        data = []

        for row in reader:
            data.append(row[1:])

    data = data[1:]

    return data


def convert_data_structure(data):
    '''
    Converts the dataset from a list of lists to a a list of dictionaries.
    '''

    l_2012, l_2013, l_2014, l_2016, l_2017 = [], [], [], [], []

    codes = []

    for row in data:

        year = row[0]
        score = row[1]
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
        if year == '2017':
            l_2017.append(d)

    data_dict = {2012: l_2012, 2013: l_2013, 2014: l_2014, 2016: l_2016, 2017: l_2017}

    codes = list(set(codes))

    return data_dict, codes


def func(args):

    pass


if __name__ == "__main__":

    input_file = 'final_data/school_data.csv'
    output_file = 'final_data/final_school_data.csv'

    data_list = create_data_list(input_file)

    data_dict = convert_data_structure(data_list)