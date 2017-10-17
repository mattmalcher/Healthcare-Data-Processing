from Functions import *

# Function to initialise mastercsv with header rows defined by schema
[col_headings, imn_schema, opd_schema, mhd_schema] = init_master_csv()

# point to JSON written out by Read_to_JSON.py
clinic_json = '../Output/clinicdata.json'

# Parse the JSON and print the number of clinic_data dictionaries found
with open(clinic_json) as data_file:
    clinic_data = json.load(data_file)
    print("\n",len(clinic_data), " Clinics read from JSON",)

# Initialise sets for clinics and years
clinics_s = set()
year_s = set()

# Iterate over clinic data, creating a de-duplicated lists of years and clinic region-name sets present in the JSON
for item in clinic_data:
    clinics_s.add(item['region']+' - '+item['clinic'])
    year_s.add(item['year'])

# Read Clinic Info from ClinicInfo.csv
all_clinics_dict = get_clinic_info()

# Generate an ordered dictionary of months using above list of lists
# (Ordered dictionary is required to maintain jan-dec ordering when doing this)
month_od = gen_ordered_dict(months)

# Initialise data_ids list - this stores the year, month & the concatenated: '<region> - <clinic name>'
# These should uniquely identify each clinic data item
data_ids = []

# Generate structure for data to be written into using the sets from the JSON
for year in year_s:
    for month in month_od:
        for clinic in clinics_s:  # Note clinic_s is '<region> - <clinic name>'
            data_ids.append([year, month, clinic])

# Generate a combined list of column headings from the col_headings (first few columns) and the schema
# This is used here purely for getting the length of the row  with which to build data_rows
combined = col_headings + imn_schema + opd_schema + mhd_schema

# Generate an empty list of lists for the data_rows so they can be indexed into
# (cant index to position in non-existing list)
# Uses list comprehensions.
data_rows = [['' for _ in range(len(combined))] for _ in range(len(data_ids))]

# Generate column indexes with which to put data into the data_rows
# Done using the lengths of the schema and col_headings items
imn_idx = len(imn_schema) + len(col_headings)
opd_idx = len(opd_schema) + imn_idx
mhd_idx = len(mhd_schema) + opd_idx

# Initialise row counter
i = 0

# Iterate over our data_identifiers
for ids in data_ids:

    # Insert the data identifiers into the first 2 items of data_row (year and month)
    data_rows[i][0:2] = ids[0:2]

    # Iterate over our clinic data items read in from the JSON
    for d_set in clinic_data:

        # If the dataset item we are on matches the data row we are on:
        # note the month (worksheet name) can be any of the alternatives listed above.
        if (d_set['year'] == ids[0]) and \
                (d_set['month'] in month_od[ids[1]]) and \
                (d_set['region']+' - '+d_set['clinic'] == ids[2]):

            # Set the region & clinic name
            data_rows[i][2] = d_set['region']
            data_rows[i][3] = d_set['clinic']

            # Get the clinic information dictionary for this region & clinic
            clin_dict = extract_clinic_info(all_clinics_dict, d_set['region'], d_set['clinic'])

            # use it to foll out the following items in the data row
            data_rows[i][5] = clin_dict['status']       # Clinic Type
            data_rows[i][6] = clin_dict['district']     # District
            data_rows[i][7] = clin_dict['funding']      # Donor
            data_rows[i][8] = clin_dict['pop']          # Est.Pop.


            # set the appropriate columns of the data row (as determined using generated indexes) to the results values
            if d_set['data']['type'] == 'Immunisation':
                data_rows[i][len(col_headings):imn_idx] = d_set['data']['results']

            elif d_set['data']['type'] == 'OPD':
                data_rows[i][imn_idx:opd_idx] = d_set['data']['results']

            elif d_set['data']['type'] == 'Motherhood':
                data_rows[i][opd_idx:mhd_idx] = d_set['data']['results']

            else:
                print(i, 'Data Incomplete')

    i += 1  # Increment data row counter

# Prune empty datarows - ignoring first 3 columns
pruned_rows = prune(data_rows, 3)

# Append the datarows to the file
append_data_rows(pruned_rows)

print('\nDone')

