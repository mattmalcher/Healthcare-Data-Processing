# Little bit of hacky script to generate a list of clinics to go in clinicdata.csv

# Function Imports
from Functions import *

clinics_s = set()
alldata = []
data2write = []

with open('Output/master.csv', newline='') as csvfile:
    next(csvfile)
    next(csvfile)
    next(csvfile)
    csvobj = csv.reader(csvfile, dialect='excel')

    # Get list of unique clinics
    for row in csvobj:
        if ('mobile' in row[6]) or ('Mobile' in row[6]):
            print(row[4] + ' - ' + row[6])
            clinics_s.add(row[4] + ' - ' + row[6])
        else:
            clinics_s.add(row[6])

        alldata.append([row[6], row[7], row[5], row[2], row[4], row[3]])


for item in clinics_s:

    for data in alldata:

        if ('mobile' in item) or ('Mobile' in item):
            print(data[4] + ' - ' + data[0])
            if data[4] + ' - ' + data[0] == item:
                print(data)
                data2write.append(data)
                break
        else:
            if data[0] == item:
                print(data)
                data2write.append(data)
                break


with open('Schema/ClinicInfo.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, dialect='excel')

    wr.writerow(['Name', 'Pop', 'Donor', 'Type', 'District', 'Region'])

    for item in data2write:
        wr.writerow(item)


