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
    # assume zipcode is NOT in multiple rate areas

    rate_area, state = get_rate_area_and_state_for_zipcode(zipcode)
    costs = []

    with open(plans_file) as plans:
        plans_reader = csv.DictReader(plans)

        for row in plans_reader:
            if row['rate_area'] == rate_area and \
                row['state'].lower() == state and \
                row['metal_level'].lower() == 'silver':
                    costs.append(float(row['rate']))
    return costs

def get_second_lowest_cost(costs):
    costs = sorted(list(set(costs)))
    if len(costs) > 1:
        return format(costs[1], '.2f')
    return None

def get_rate_area_and_state_for_zipcode(zipcode):
    rate_area, state = '', ''

    with open(zipcode_data_file) as zip_data:
        zip_data_reader = csv.DictReader(zip_data)

        for row in zip_data_reader:
            if row['zipcode'] == zipcode:
                rate_area = row['rate_area']
                state = row['state'].lower()

    return rate_area, state

def write_new_file():
    field_names = ['zipcode', 'rate']

    with open(output_file, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, fieldnames=field_names)
        writer.writeheader()

    with open(input_file) as in_file:
        in_reader = csv.DictReader(in_file)

        for row in in_reader:
            zipcode = row['zipcode']
            rate = None

            if not zipcode_in_multiple_rate_areas(zipcode):
                costs = get_all_costs_for_zipcode(zipcode)
                rate = get_second_lowest_cost(costs)

            with open(output_file, 'a', newline='') as out_file:
                writer = csv.DictWriter(out_file, fieldnames=field_names)
                out_row = {'zipcode': zipcode}
                if rate:
                    out_row['rate'] = rate
                writer.writerow(out_row)
