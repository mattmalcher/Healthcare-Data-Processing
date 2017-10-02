from Functions import *

clinic_json = 'Output/clinicdata.json'

with open(clinic_json) as data_file:

    clinic_data = json.load(data_file)
    countf = len(clinic_data)

    print("Number of clinics: ",countf)


# Get list of clinics

# Get list of years there are data for

# Get list of months there are data for

# Initialise CSV file, writing headers from schema

# Iterate over years then months, then clinics, printing rows to csv


