# School Score Index
#
# Something Creative

import csv
import time

start_time = time.time()

RATINGS = {
'NO DATA AVAILABLE': None, 'NOT ENOUGH DATA': None, 'INCOMPLETE DATA': None, 'NDA': None, '': None, ' ': None,
'FAR BELOW AVERAGE': 0, 'BELOW AVERAGE': 1, 'AVERAGE': 2, 'ABOVE AVERAGE': 3, 'FAR ABOVE AVERAGE': 4,
'FAR-BELOW-AVERAGE': 0, 'BELOW-AVERAGE': 1, 'AVERAGE': 2, 'ABOVE-AVERAGE': 3, 'FAR-ABOVE-AVERAGE': 4,
'NOT YET ORGANIZED': 0, 'PARTIALLY ORGANIZED': 1, 'MODERATELY ORGANIZED': 2, 'ORGANIZED': 3, 'WELL ORGANIZED': 4,
'NOT-YET-ORGANIZED': 0, 'PARTIALLY-ORGANIZED': 1, 'MODERATELY-ORGANIZED': 2, 'ORGANIZED': 3, 'WELL-ORGANIZED': 4,
'EMERGING': 1, 'DEVELOPING': 2, 'STRONG': 3, 'EXCELLING': 4,
'VERY WEAK': 0, 'WEAK': 1, 'NEUTRAL': 2, 'STRONG': 3, 'VERY STRONG': 4,
'VERY-WEAK': 0, 'VERY-STRONG': 4
}

RATINGS_LWR = {}
for key in RATINGS.keys():
    lwr_key = key.lower()
    RATINGS_LWR[lwr_key] = RATINGS[key]

KEYS = [
'Zip', 'Student_Growth_Rating', 'Student_Attainment_Rating',
'Culture_Climate_Rating', 'Creative_School_Certification', 'School_Survey_Involved_Families',
'School_Survey_Supportive_Environment', 'School_Survey_Ambitious_Instruction',
'School_Survey_Effective_Leaders', 'School_Survey_Collaborative_Teachers',
'School_Survey_Safety', 'School_Survey_School_Community',
'School_Survey_Parent_Teacher_Partnership', 'School_Survey_Quality_Of_Facilities',
# NEWER VERS ^
# OLDER VERS >
'My Voice, My School Overall Rating', 'Involved Family', 'Supportive Environment',
'Ambitious Instruction', 'Effective Leaders', 'Collaborative Teachers', 'Safe',
'School Community', 'Parent-Teacher Partnership', 'Quality of Facilities',
'Creative Schools Certification', 'ZIP Code', 'Safety Icon', 'Family Involvement Icon',
'Environment Icon', 'Instruction Icon', 'Leaders Icon', 'Parent Engagement Icon',
'Parent Environment Icon', 'Growth Overall Level', 'Student Performance Level',
'Overall Foundation', 'Involved Families', 'Supportive Environment', 'Ambitious Instruction',
'Effective Leaders', 'Collaborative Teachers', 'Safety',
# Lat/Long >
'Latitude', 'Longitude', 'School_Longitude', 'School_Latitude'
]

KEYS_LWR = []
for key in KEYS:
    KEYS_LWR.append(key.lower())

FILES = [
'school_reports/2012.csv',
'school_reports/2013.csv',
'school_reports/2014.csv',
'school_reports/2016.csv',
]


def create_reports(KEYS_LWR, FILES):
    '''
    Takes the csv files and creates a report dictionary.
    '''
    reports = {}

    for year_file in FILES:

        with open(year_file, 'r') as input_file:
            # reader = csv.DictReader(input_file, skipinitialspace=True)
            # report = [{key: value for key, value in row.items()} for row in reader]
            report = [{k: v for k, v in row.items()}
                for row in csv.DictReader(input_file, skipinitialspace=True)]


            mini_report = []
            for d in report:
                mrd = {}
                for k in d.keys():
                    if k.lower() in KEYS_LWR:
                        mrd[k.lower()] = d[k].lower()
                    if k.lower()[:-1] in KEYS_LWR:
                        mrd[k.lower()] = d[k].lower()
                mini_report.append(mrd)

            year = int(year_file[-8:-4])
            reports[year] = mini_report

    return reports


def calculate_score(school, RATINGS_LWR):
    '''
    Calculate an overall score for the quality of a school.

    Inputs:
        school (dict)

    Returns;
        score_pct (int)
    '''
    score = 0
    total = 0
    school_ratings = {}
    not_keys = ['zip code', 'zip', 'latitude', 'longitude',
                'school_longitude', 'school_latitude']
    for key in school.keys():
        if not key in not_keys:
            school_ratings[key] = RATINGS_LWR[school[key]]
            if not school_ratings[key] == None:
                score += school_ratings[key]
                total += 4

    if total == 0:
        return None
    else:
        score_pct = score / total * 100

    return int(score_pct)


def create_index(reports, RATINGS_LWR):
    '''
    Takes the info from the reports and creates a ranking for each school.
    '''
    index = {}
    for year in reports.keys():
        report = reports[year]
        l = []

        for school in report:
            if 'zip' in school.keys():
                school_zip = school['zip']
            if 'zip code' in school.keys():
                school_zip = school['zip code']
            if 'latitude' in school.keys():
                school_lat = school['latitude']
                school_lon = school['longitude']
            if 'school_latitude' in school.keys():
                school_lat = school['school_latitude']
                school_lon = school['school_longitude']
            school_score = calculate_score(school, RATINGS_LWR)
            if not school_score == None:
                d = {'zip': int(school_zip), 'score': school_score,
                     'lat': float(school_lat), 'lon': float(school_lon)}
                l.append(d)

        index[year] = l

    return index


def create_zip_list(index):
    '''
    Makes a list of all the zip codes in the inputted dict.

    Returns: list of zip codes
    '''
    zipcodes = []
    for year in index:
        for school in index[year]:
            zipcode = school['zip']
            if not zipcode in zipcodes:
                zipcodes.append(zipcode)
    return zipcodes


def aggregate_by_zip(index, zipcodes):
    '''
    Make a new dictionary with only one entry per zipcode.
    Takes the average score for each school in a zipcode.
    '''
    aggregated_index = {}
    for year in index:
        d = {}
        for zipcode in zipcodes:
            d[zipcode] = [0,0]
        aggregated_index[year] = d

    for year in index:
        for school in index[year]:
            zipcode = school['zip']
            aggregated_index[year][zipcode][0] += school['score']
            aggregated_index[year][zipcode][1] += 1

    for year in aggregated_index:
        for zipcode in aggregated_index[year]:
            score = aggregated_index[year][zipcode]
            if score == [0, 0]:
                aggregated_index[year][zipcode] = None
            else:
                aggregated_index[year][zipcode] = int(score[0] / score[1])

    return aggregated_index


def create_2015_data(aggregated_index, zipcodes):
    '''
    Since data for 2015 is missing, we will take the avg
    for the 2014 and 2016 data to represent 2015
    '''
    aggregated_index[2015] = {}
    for zipcode in zipcodes:
        if not aggregated_index[2014][zipcode] == None:
            if not aggregated_index[2016][zipcode] == None:
                avg_score = ( aggregated_index[2014][zipcode]
                            + aggregated_index[2016][zipcode] ) / 2
                aggregated_index[2015][zipcode] = int(avg_score)

    return aggregated_index


def write_ag_to_csv(aggregated_index):
    '''
    Create a csv file for each year from the nested dictionaries.
    '''
    filename = 'data/school_quality.csv'
    with open(filename, 'w') as output_file:
        for year in aggregated_index:
            # filename = 'school_index/' + str(year) + '_index.csv'
            year_dict = aggregated_index[year]
            # with open(filename, 'w') as output_file:
            for key in year_dict.keys():
                output_file.write(
                str(year) + ', '
                + str(key) + ', '
                + str(year_dict[key]) + '\n')


def write_index_to_csv(index):
    '''
    Create a csv file for each year from the nested dictionaries.
    '''
    filename = 'data/school_quality.csv'
    with open(filename, 'w') as output_file:
        for year in index:
            year_list = index[year]
            for school in year_list:
                output_file.write(
                str(year) + ', '
                + str(school['lat']) + ', '
                + str(school['lon']) + ', '
                + str(school['zip']) + ', '
                + str(school['score']) + '\n'
                )


if __name__ == "__main__":

    reports = create_reports(KEYS_LWR, FILES)

    index = create_index(reports, RATINGS_LWR)

    write_index_to_csv(index)

    # zipcodes = create_zip_list(index)
    #
    # aggregated_index = aggregate_by_zip(index, zipcodes)
    #
    # aggregated_index = create_2015_data(aggregated_index, zipcodes)
    #
    # write_ag_to_csv(aggregated_index)

    print("--- %s seconds ---" % (time.time() - start_time))
