# Module Imports
import csv
import re
import json
import os
import collections
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


def readschema(filename):
    # Function to read the schema files (which define where to look for all the data) into lists

    csvcontents = []

    with open(filename, newline='') as csvfile:

        csvobj = csv.reader(csvfile, delimiter=',', quotechar='|')

        for row in csvobj:
            csvcontents.append(row)

    return csvcontents


def getschema(w_sheet):
    # Function which takes a worksheet and returns the appropriate schema

    # Look in Cell B5 which contains different things for each sheet type
    sheet_indicator = w_sheet['B5'].value

    if sheet_indicator == 'EPI: CHILDREN':
        schema = readschema('Schema/Immunisation Schema_01.csv')
        schema_id = 'Immunisation Schema_01'
        s_type='Immunisation'

    elif sheet_indicator == 'OUTPATIENT - CURATIVE SERVICES':
        schema = readschema('Schema/OPD Schema_01.csv')
        schema_id = 'OPD Schema_01'
        s_type = 'OPD'

    elif sheet_indicator == 'SAFE MOTHERHOOD PROGRAMME':
        schema = readschema('Schema/Motherhood Schema_01.csv')
        schema_id = 'Motherhood Schema_01'
        s_type = 'Motherhood'

    else:
        print('Error - Sheet format not identified')

    return s_type, schema, schema_id


def year_from_fname(fname):
# Use regular expressions to extract *20XX* year from a filename where XX is two numbers
    try:
        re_year = re.search(r".*(20[0-9]{2}).*", fname).group(1)
    except AttributeError:
        print('Year Not Found in Filename')
        re_year = 0

    year = int(re_year)

    return year

# Define a data class for storing clinic data
# Not used as custom classes cannot be serialised to json without more work
# class CDO:
#
#     # Initialise items of the class with the clinic
#     def __init__(self, name, year, month):
#         self.name = name  # Clinic Name
#         self.year = year  # Year of Data Collection
#         self.month = month  # Month of Data Collection
#
#         self.region = ''    #
#         self.clin_typ = ''
#
#         # Dictionary for data, containing type (immunisation, motherhood, opd)
#         self.data = {'type': '', 'schema_id': 0, 'results': []}
#
#

def schema2header(schema):
    # function to format ouput of readschema to some nice headers

    headers = [] #Empty list to fill with headers

    for item in schema:
        # Schema consists of a list of lists, join the items in the inner lists using newline chars to generate headers
        headers.append('\n'.join(item[1:-1]))

    return headers


def init_mastercsv():
    # Initialise CSV file, writing headers from schema
    with open('Output/master_out.csv', 'w', newline='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(['Compiled healthcare data from files in \'Input\'',])

        # Column Headings for Non-Schema Rows
        col_headings = ['Year', 'Month','Region', 'Clinic Type',
                        'District', 'Donor', 'Location of clinic', 'Est.Pop.']

        # Read in schema as lists
        imn_schema = schema2header(readschema('Schema/Immunisation Schema_01.csv'))
        opd_schema = schema2header(readschema('Schema/OPD Schema_01.csv'))
        mhd_schema = schema2header(readschema('Schema/Motherhood Schema_01.csv'))

        # Combine the lists& column headings
        combined_schema = col_headings + imn_schema + opd_schema + mhd_schema

        wr.writerow(combined_schema)

    return col_headings, imn_schema, opd_schema, mhd_schema


def append_datarows(rows):
    # Function to append rows to the master_out csv initialised by init_mastercsv

    with open('Output/master_out.csv', 'a', newline='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        for row in rows:
            wr.writerow(row)