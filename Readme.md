
#Introduction
A small collection of scripts for reading and compiling healthcare data.
This readme is primarily intended to capture notes and useful references.

##Task
Help produce some scripts to tidy up and compile the Somali Healthcare Data.

#Notes on Software
##Reading Excel Files Using Python
The people at http://www.python-excel.org recommends openpyxl for reading and writing Excel 2010 files.
This can be installed using `pip3 install openpyxl`.

Documentation at: https://openpyxl.readthedocs.org

## Compiling the script using Nuitka

Documentation at: http://nuitka.net/doc/user-manual.html 
It's quite easy to use to produce distributable C executables from python code.

Install Nuitka using:

`pip3 install -U nuitka`

Make sure you have a compiler set up
* If on macOS you need Xcode with gcc set up
* If on Windows you can install Visual Studio Community edition

Compile a script, including all its dependencies using:

`nuitka --recurse-all RunScript.py` 

Run the resulting executable:

`./RunScript.exe`

## Compiling the script using PyInstaller

`pip3 install pyinstaller`

`pyinstaller RunScript.py`


# Problems with the data 
There are several things about the way the data is captured which present challenges when
attempting to clean and process it. The scripts attempt to handle these but ultimately these issues limit how useful a 
programmatic approach to cleaning the data will be.

In no particular order:

1. There is no year field in the templates, but there will be data from multiple years.
This means that the year data has to be extracted from the filename which is not particularly robust.

* The year information could easily be removed by renaming the file
* The filename needs to be a consistent format to extract the year data from it. i.e. always 20XX or XX which is easy to forget.

2. There is inconsistency in the template:

* The 'Region Name:' data is in D1 in the Safe Motherhood and OPD sheets, whilst it is in C1 in Immunisation
* Totals are in column 'F' in Immunisation, 'W' in Safe Motherhood and 'I' in OPD. (Are totals even used?)

3. There is inconsistency in the way the templates are filled out. Where data is missing,
* Sometimes the cells are left empty, 
* Sometimes they are filled with a hyphen '-'
* Sometimes they are filled with a '0'
* Sometimes there is data present in the column, but there is no 'Name of MCH' data in row 4

4. The way missing months are represented varies. 
* Sometimes there is a completely blank sheet
* Sometimes there is a sheet with nothing filled in


5. There are many variations on the spellings of single locations. This makes it difficult to group data appropriately,
as well as making it tricky to do lookups against the name. I have decided not to add error handling for this because it 
encourages sloppy data input.

* For example in the provided example files there are five different spellings of 'Yagori':
 Yagori	
 Yogori	
 Yogroi	
 Yogri	
 Yagoori

6. The questions are numbered / lettered in such a way that there is not a unique identifier for each question.
* For example in the OPD spreadsheets, does 4.3.4 refer to the Under 5 or Over 5 ARI Number?
* Further, some lists take the format 4.3.4, 4.3.5 while others are 10a, 10b etc.

7. The spreadsheets include numerous Merged cells which makes it harder to extract the labels for the data.
* To work around this the script uses manually edited schema files as a key to map data values to labels. 


#Current Issues / To Do
These items are not presently handled by the script or are known problems.

* Handling of duplicate files - some error indication

* A lookup on clinic data - sponsor, population etc
* Add in a pointer to the filename for each item of data

* update year_from_fname to handle 20188 case (reports 2018 not error)

#MPM Tasks
Produce examples sheet showing examples of each error and how it can be fixed

#Somalia Tasks
Clean Data as per the examples sheet


![alt text][logo]

[logo]: https://github.com/mattmalcher/Healthcare-Data-Processing/images/ImportLog.png "Logo Title Text 2"