# Script for scraping & compiling healthcare data from excel files

# Function Imports
from Functions import *

# Generate list of input files
path = 'Input/'
f_list = os.listdir(path)

# List of valid sheet names in the input files
validsheets = ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
               'January','February', 'March', 'April','May','June','July','August','September',
               'October', 'November', 'December']

# Iterate over the files
for in_file in f_list:

    # Load workbook object - using data_only=True to get calculated values not formulae
    w_book = load_workbook(path+in_file, data_only=True)

    # Feed the first worksheet into getschema and get back the schema
    schema = getschema(w_book.worksheets[0])

    # For each worksheet in the file/'workbook'...
    for w_sheet in w_book:

        # Check if it is a month sheet, If its not, print a descriptive error
        if w_sheet.title not in validsheets:
            print(w_sheet.title,'not in list of valid sheet names: ',validsheets)

        # otherwise get on with it
        else:
            print('\n',in_file, ' - ',w_sheet.title)

            # ...iterate over the schema, storing results
            for scheme in schema:
                value = w_sheet[scheme[0]].value

                try:
                    name = scheme[1]+' '+scheme[2]+' '+scheme[3]
                except IndexError:
                    name = scheme[1]+' '+ scheme[2]

                print(value,'   ', name)





