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

clinics=[

]

# Generate an ordered dictionary of months using above list of lists
month_od = genOrderedDict(months)

# Initialise data_ids list - this stores the year, month & clinic name
# These should uniquely identify each clinic data item
data_ids = []

# Generate structure for data to be written into
for year in year_s:
    for month in month_od:
        for clinic in clinics_s:
            data_ids.append([year, month, clinic])

# Generate a combined list of column headings from the col_headings (first few columns) and the schema
combined = col_headings + imn_schema + opd_schema + mhd_schema

# Generate an empty list of lists for the data_rows so they can be indexed into
# Uses list comprehensions.
data_rows = [['' for _ in range(len(combined))] for _ in range(len(data_ids))]

# Initialise row counter
i = 0

# Generate indexes with which to put data into the data_rows
# Done using the lengths of the schema and col_headings items
imn_idx = len(imn_schema) + len(col_headings)
opd_idx = len(opd_schema) + imn_idx
mhd_idx = len(mhd_schema) + opd_idx

# Iterate over our data_identifiers
for ids in data_ids:

    # Insert the data identifiers into the first 3 items of data_row
    data_rows[i][0:3] = ids[0:3]

    # Iterate over our clinic data items read in from the JSON
    for d_set in clinic_data:

        # If the dataset item we are on matches the data row we are on:
        # note the month (worksheet name) can be any of the alternatives listed above.
        if (d_set['year'] == ids[0]) and \
                (d_set['month'] in month_od[ids[1]]) and \
                (d_set['name'] == ids[2]):

            # set the appropriate bits of the data row to the results value
            if d_set['data']['type'] == 'Immunisation':
                data_rows[i][len(col_headings):imn_idx] = d_set['data']['results']

            elif d_set['data']['type'] == 'OPD':
                data_rows[i][imn_idx:opd_idx] = d_set['data']['results']

            elif d_set['data']['type'] == 'Motherhood':
                data_rows[i][opd_idx:mhd_idx] = d_set['data']['results']

            else:
                print(i, 'Data Incomplete')

    i += 1  # Increment data row counter


# clean rows

# Prune empty datarows - ignoring first 3 columns
pruned_rows = prune(data_rows, 3)

# Append the datarows to the file
append_datarows(pruned_rows)



