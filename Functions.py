# Module Imports
import csv
import re
import json
import os
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
# Use regular expressions to extract a 20xx year from a filename

    year=2016


    return(year)

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
