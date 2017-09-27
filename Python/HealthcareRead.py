# Script for scraping & compiling healthcare data from excel files

# Module Imports
from openpyxl import load_workbook
import os

path = '../Input/'
items = os.listdir(path)

# Generate list of valid input files


# Import Function

from openpyxl import Workbook

w_book = load_workbook(path+items[0])

for sheet in w_book.worksheets:

    print(sheet.title)

    region_name=sheet['C1']

    sheet_data=sheet['C':'D']

    print(sheet_data[0])

    sheet['B11'].value




# Processing


# Compile & Output