# little tool to speed up generating schema of what data is where in the excel files

# Module Imports
from openpyxl import load_workbook
import os

path = '../Input/'
items = os.listdir(path)

# Generate list of valid input files


# Import Function

from openpyxl import Workbook

w_book = load_workbook(path+items[2])

i = 1
cell_A = ' '
cell_B = ' '
cell_C = ' '

rowlist = []

sheet= w_book.worksheets[0]

print(sheet.title)

for i in range(1, 50):

    if sheet['A' + str(i)].value is not None:

        cell_A = str(sheet['A' + str(i)].value)

    if sheet['B' + str(i)].value is not None:

        cell_B = str(sheet['B' + str(i)].value)

    if sheet['C' + str(i)].value is not None:

        cell_C = str(sheet['C' + str(i)].value)

    rowlist.append(['D'+str(i), cell_A, cell_B, cell_C])


for row in rowlist:
    print(row[0], ', ', row[1] + ', ' + row[2] + ', ' + row[3])

with open("Messy Schema.csv", "w") as text_file:
    for row in rowlist:
        print(row[0],', ',row[1]+', '+row[2]+', '+row[3], file=text_file)