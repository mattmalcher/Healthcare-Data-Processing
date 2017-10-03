from Functions import *

# Function to initialise mastercsv with header rows defined by schema
[col_headings, imn_schema, opd_schema, mhd_schema] = init_mastercsv()

# point to JSON written out by Read_to_JSON.py
clinic_json = 'Output/clinicdata.json'

# Parse the JSON and print the number of clinic_data dictionaries found
with open(clinic_json) as data_file:
    clinic_data = json.load(data_file)
    print("Number of clinics: ", len(clinic_data))

# Get list of unique clinics, years and months
clinics_s = set()
year_s = set()
# month_s = set()

# Create de-duplicated lists of years and clinic names present in input data
for item in clinic_data:
    clinics_s.add(item['name'])
    year_s.add(item['year'])
    # month_s.add(item['month'])

# # Print the de-duplicated list for inspection
# print(sorted(year_s))
# print(sorted(month_s))
# print(sorted(clinics_s))

# Need a way of grouping alternative strings for months
months = [
            ['Jan', 'jan', 'January', 'january'],
            ['Feb', 'feb', 'February', 'february', 'Febuary', 'febuary'],
            ['Mar', 'mar', 'March', 'march'],
            ['Apr', 'apr', 'April', 'april'],
            ['May', 'may'],
            ['Jun', 'jun', 'June', 'june'],
            ['Jul', 'jul'],
            ['Aug', 'aug', 'August', 'august'],
            ['Sep', 'sep', 'Sept', 'sept', 'september', 'September'],
            ['Oct', 'oct', 'October', 'october'],
            ['Nov', 'nov', 'November', 'november'],
            ['Dec', 'dec', 'December', 'december']]

# Insert each set of items into an ordered dictionary
month_od = collections.OrderedDict()
for item in months:
    month_od[item[0]] = item

# Initialise data_ids list - this stores the year, month & clinic name
# These should uniquely identify each clinic data item
data_ids = []

# Generate structure for data to be written into
for year in year_s:
    for month in month_od:
        for clinic in clinics_s:
            data_ids.append([year, month, clinic])

a = col_headings + imn_schema + opd_schema + mhd_schema
data_rows = [['' for _ in range(len(a))] for _ in range(len(data_ids))]

i = 0
col_offset = len(col_headings)-len(data_ids[0])-1

imn_idx = len(imn_schema) + col_offset
opd_idx = len(opd_schema) + imn_idx
mhd_idx = len(mhd_schema) + opd_idx

for ids in data_ids:

    for d_set in clinic_data:

        if (d_set['year'] == ids[0]) and \
                (d_set['month'] in month_od[ids[1]]) and \
                (d_set['name'] == ids[2]):

            if d_set['data']['type'] == 'Immunisation':
                data_rows[i][col_offset+1:imn_idx] = d_set['data']['results']

            elif d_set['data']['type'] == 'Motherhood':
                data_rows[i][imn_idx+1:opd_idx] = d_set['data']['results']

            elif d_set['data']['type'] == 'OPD':
                data_rows[i][opd_idx+1:mhd_idx] = d_set['data']['results']

            else:
                print(i, 'Data Incomplete')

    i += 1  # Increment data row counter

Lmerge = [x + y for x,y in zip(data_ids, data_rows)]

append_datarows(Lmerge)



