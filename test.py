from slcsp import (
    zipcode_in_multiple_rate_areas
    )
import csv

input_file = 'slcsp.csv'
zipcode_data_file = 'zips.csv'

def get_zipcodes_in_multiple_rate_areas():
    duplicates = []
    with open(input_file) as in_file:
        in_reader = csv.DictReader(in_file)

        for row in in_reader:
            zipcode = row['zipcode']
            count = 0

            with open(zipcode_data_file) as zip_data:
                zip_reader = csv.DictReader(zip_data)
                for other_row in zip_reader:
                    other_zipcode = other_row['zipcode']
                    if zipcode == other_zipcode:
                        count += 1

            if count > 1:
                duplicates.append(zipcode)
            #print('zipcode: {}, count: {}'.format(zipcode, count))
    return duplicates

def test_zipcode_in_multiple_rate_areas():
    test_zip = '64148'
    
    assert zipcode_in_multiple_rate_areas(test_zip) == False