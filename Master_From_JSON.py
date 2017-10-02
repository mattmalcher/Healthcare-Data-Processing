from Functions import *

clinic_json = 'Output/clinicdata.json'

with open(clinic_json) as data_file:

    clinic_data = json.load(data_file)
    countf = len(clinic_data)

    print("Number of clinics: ", countf)

# Get list of unique clinics, years and months

clinics_s = set()
year_s = set()
month_s = set()

for item in clinic_data:
    clinics_s.add(item['name'])
    year_s.add(item['year'])
    month_s.add(item['month'])


print(sorted(year_s))
print(sorted(month_s))
print(sorted(clinics_s))

# Need a way of grouping alternative strings for months and names, perhaps:
months={
    '1': ['jan','Jan','January','january'],
    '2': ['feb',],
    '3': ['mar',],
    '4': ['apr',],
    '5': ['may',],
    '6': ['jun',],
    '7': ['jul',],
    '8': ['aug',],
    '9': ['sep','sept','Sep','september','September'],
    '10': ['oct',],
    '11': ['nov'],
    '12': ['dec']}


for month in months:
    if '' in month:
        print ''


# Initialise CSV file, writing headers from schema


# Iterate over years then months, then clinics, printing rows to csv
