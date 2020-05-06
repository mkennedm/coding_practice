
import csv
from datetime import datetime

plans_file = 'plans.csv'
input_file = 'slcsp.csv'
zipcode_data_file = 'zips.csv'

def gen_output_file_name():
    time_str = datetime.now().strftime('%Y%m%d%H%M%S')
    return 'output_slcsp_{}.csv'.format(time_str)

output_file = gen_output_file_name()

def zipcode_in_multiple_rate_areas(zipcode):
    with open(zipcode_data_file) as zip_data:
        zip_data_reader = csv.DictReader(zip_data)
        count = 0

        for row in zip_data_reader:
            zip_data_zipcode = row['zipcode']
            if zipcode == zip_data_zipcode:
                count += 1
                if count > 1:
                    return True

        return False

def get_all_costs_for_zipcode(zipcode):
    # zipcode is NOT in multiple rate areas

    rate_area = ''

    with open(zipcode_data_file) as zip_data:
        zip_data_reader = csv.DictReader(zip_data)

        for row in zip_data_reader:
            if row['zipcode'] == zipcode:
                rate_area = row['rate_area']

    return []

def get_rate_area_for_zipcode(zipcode):
    rate_area = ''

    with open(zipcode_data_file) as zip_data:
        zip_data_reader = csv.DictReader(zip_data)

        for row in zip_data_reader:
            if row['zipcode'] == zipcode:
                rate_area = row['rate_area']

    return rate_area