# Script for scraping & compiling healthcare data from excel files

# Function Imports
from Functions import *

# Initialise the Import Log
init_import_log()

# Generate list of input files
path = '../Input/'
f_list = os.listdir(path)
f_count = 0

# List of valid sheet names in the input files
# Uses list comprehension to generate flat list of months from nested list in Functions.py
valid_sheets = [inner for outer in months for inner in outer]

# Empty list to store clinic data objects in
ClinicData = []

# Iterate over the files
for in_file in f_list:

    # if the file is not an .xlsx then skip to the next one
    if not in_file.endswith('.xlsx'):
        message = 'File Skipped'
        write_to_log(['Error', message, in_file, 'N/A'])
        continue

    # Increment the file counter
    f_count += 1

    # Get year from the filename using regular expressions
    f_year = year_from_fname(in_file)

    # Load workbook object - using data_only=True to get calculated values not formulae
    w_book = load_workbook(path + in_file, data_only=True)

    # Feed the first worksheet into get_schema and get back the schema
    [s_type, schema, schema_id] = get_schema(w_book.worksheets[0])

    # For each worksheet in the file/'workbook'...
    for w_sheet in w_book:

        # Get Region Name from C1 or D1 as appropriate
        C1 = w_sheet['C1'].value
        D1 = w_sheet['D1'].value

        if C1 is None and D1 is None:
            region = 'Region Name Not Found in Worksheet'
            print('Error: '+region)
            write_to_log(['Error', region, in_file, w_sheet])

        elif C1 is not None:
            region = C1

        elif D1 is not None:
            region = D1

        # Initialise list of data columns
        data_cols = []

        print('\n\n', in_file, ' - ', w_sheet.title)

        # Check if it is a month sheet, If its not, print a descriptive error
        if w_sheet.title not in valid_sheets:
            message = 'Not in list of valid sheet names (Months).'
            print('Error: ' + message)
            write_to_log(['Error', message, in_file, w_sheet])
            continue  # otherwise get on with it

        # Key Assumption!
        # Each column, from D4 onwards with something in row 4 has data,
        # if there is a blank cell in this row 4 this marks the last column.

        # Get the column letter for the max column in the sheet
        mx_col = get_column_letter(w_sheet.max_column)

        # If this is A then the sheet is empty - add a message saying so and go on to next sheet
        if mx_col == 'A':
            message = 'Empty Sheet'
            print('Error: ' + message)
            write_to_log(['Error', message, in_file, w_sheet])
            continue

        # Get the cell range which includes the potential headers
        cell_range = w_sheet['D4':mx_col + '4']

        try:
            # If there is nothing there, print an error.
            if (cell_range[0][0].value is None) or (cell_range[0][0].value is "TOTAL"):
                message = "Blank Column Header(s)"
                print('Error: ' + message)
                write_to_log(['Error', message, in_file, w_sheet])

        except IndexError:
            message = "Invalid Format Column Header(s)"
            print('Error: ' + message)
            write_to_log(['Error', message, in_file, w_sheet])

        # Iterate over the potential headers
        for cell in cell_range[0]:

            # If we hit an empty cell - append a message saying the last column has been reached
            if cell.value is None:
                break  # Then exit the for loop
            else:
                # Otherwise, append the header and its column index to the results array.
                data_cols.append([cell.value, cell.column])

        # Now, iterate over the columns we *HAVE* found data in, and read them in as per the schema.
        for column in data_cols:

            schema_data = []

            for item in schema:

                try:
                    # Try using the schema to get a value
                    value = w_sheet[column[1]+item[0]].value

                except ValueError:
                    # If not, append an informative error.
                    value = 'Value Not Found - Check Schema'
                    print('Error: ' + value)
                    write_to_log(['Error', value, in_file, w_sheet])

                schema_data.append(value)

                try:
                    name = item[1:-1]

                except IndexError:
                    name = ['Schema Format Wrong']
                    print('Error: ' + name)
                    write_to_log(['Error', name, in_file, w_sheet])

                # print(value,'   ', name)

            # Store the schema data & metadata in a dictionary which can be serialised to a JSON
            ClinicDict = {
                'region': region,
                'clinic': w_sheet[column[1]+'4'].value,
                'year': f_year,
                'month': w_sheet.title,
                'data': {
                    'type': s_type,
                    'results': schema_data,
                    'schema_id': schema_id
                    },
                'f_name': in_file,
                'w_sheet': w_sheet.title
                }

            # Add the dictionary to the list of dictionaries to be serialised.
            ClinicData.append(ClinicDict)

            # Print a message indicating an item has been added to the JSON
            message = "Data Successfully Extracted"
            print(message)
            write_to_log(['Success', message, in_file, w_sheet])

if f_count == 0:
    message = 'No valid files found in \'Input\' folder'
    print('\n' + message)
    write_to_log(['Error', message, 'N/A', 'N/A'])
    exit() # Not much point going futher if there is no identified input

else:
    message = 'Extraction Complete for files in \'Input\' folder'
    print('\n'+message)
    write_to_log(['Success', message, 'N/A', 'N/A'])


with open('../Output/clinicdata.json', 'w') as outfile:
    json.dump(ClinicData, outfile)

message = 'Data written to \'Output/clinicdata.json\''
print('\n'+message)
write_to_log(['Success', message, 'N/A', 'N/A'])