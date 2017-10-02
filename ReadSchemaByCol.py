# Script for scraping & compiling healthcare data from excel files

# Demo version which iterates over files in input and prints out the columns where there is data.

# Function Imports
from Functions import *

# Generate list of input files
path = 'Input/'
f_list = os.listdir(path)

# List of valid sheet names in the input files
validsheets = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
               'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
               'October', 'November', 'December']

# Iterate over the files
for in_file in f_list:

    if not in_file.endswith('.xlsx'): continue

    # Load workbook object - using data_only=True to get calculated values not formulae
    w_book = load_workbook(path + in_file, data_only=True)

    # Feed the first worksheet into getschema and get back the schema
    schema = getschema(w_book.worksheets[0])

    # For each worksheet in the file/'workbook'...
    for w_sheet in w_book:

        datacols = []

        print('\n\n', in_file, ' - ', w_sheet.title)

        # Check if it is a month sheet, If its not, print a descriptive error
        if w_sheet.title not in validsheets:
            print('Error - Not in list of valid sheet names.')

        # otherwise get on with it
        else:

            # Key Assumptions!
            # Each column, from D4 onwards with something in row 4 has data,
            # if there is a blank cell in this row 4 this marks the last column.


            # Get the column letter for the max column in the sheet
            mx_col = get_column_letter(w_sheet.max_column)

            # If this is A then the sheet is empty - add a message saying so and go on to next sheet
            if mx_col == 'A': print('Error - Empty Sheet'); continue

            # Get the cell range which includes the potential headers
            cell_range = w_sheet['D4':mx_col + '4']

            # print(cell_range)

            if cell_range[0][0].value is None:
                print("Error - Blank Column Header(s)")


            # Iterate over the potential headers
            for cell in cell_range[0]:

                # If we hit an empty cell - append a message saying the last column has been reached
                if cell.value is None:
                    break  # Then exit the loop
                else:
                    # Otherwise, append the header and its column index to the results array.
                    datacols.append([cell.value, cell.column])

        # Now, iterate over the columns we *HAVE* found data in, and read them in as per the schema.
        for column in datacols:

            for item in schema:
                value = w_sheet[column[1]+item[0]].value



                try:
                    name = item[1:-1]
                except IndexError:
                    name = ['Error - Schema Format Wrong']

                print(value,'   ', name)






