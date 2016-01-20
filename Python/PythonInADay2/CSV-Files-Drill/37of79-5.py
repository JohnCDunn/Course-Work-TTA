import os
# The path to the script
currentPath = os.path.dirname( os.path.abspath("__file__"))
print currentPath

# Make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv

# Open the file
cscFile = open(outputCsv, "wb")

# Create writer object
writer = csv.writer(csvfile, delimiter=',')
 

#  Result from above
#  C:\Users\Student\Documents\All My Essays\Python
#  C:\Users\Student\Documents\All My Essays\Python/spreadsheet.csv

#Traceback (most recent call last):
#  File "C:\Users\Student\Documents\All My Essays\Python\37of79-5.py", line 14, in <module>
#    writer = csv.writer(csvfile, delimiter=',')
#NameError: name 'csv' is not defined
