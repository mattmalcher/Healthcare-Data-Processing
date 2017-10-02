# Module Imports
import csv
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
        schema = readschema('Schema/Immunisation Schema.csv')

    elif sheet_indicator == 'OUTPATIENT - CURATIVE SERVICES':
        schema = readschema('Schema/OPD Schema.csv')

    elif sheet_indicator == 'SAFE MOTHERHOOD PROGRAMME':
        schema = readschema('Schema/Motherhood Schema.csv')

    else:
        print('Error - Sheet format not identified')

    return schema