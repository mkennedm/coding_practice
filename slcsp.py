
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
    with open(input_file) as in_file:
        rate_reader = csv.DictReader(in_file)
        for row in rate_reader:
            print(row['zipcode'])