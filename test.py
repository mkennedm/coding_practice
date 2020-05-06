from slcsp import (
    zipcode_in_multiple_rate_areas,
    get_rate_area_and_state_for_zipcode
    )
import csv

input_file = 'slcsp.csv'
zipcode_data_file = 'zips.csv'
single_occurrence_zip = '64148'

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

    return duplicates

def test_zipcode_in_multiple_rate_areas():
    assert zipcode_in_multiple_rate_areas(single_occurrence_zip) == False

    duplicates = get_zipcodes_in_multiple_rate_areas()

    for zip in duplicates:
        assert zipcode_in_multiple_rate_areas(zip)

def test_get_rate_area_and_state_for_zipcode():
    assert get_rate_area_and_state_for_zipcode(single_occurrence_zip) == ('3', 'MO')