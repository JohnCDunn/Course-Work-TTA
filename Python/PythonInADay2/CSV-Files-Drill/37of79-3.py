import os
# The path to the script
currentPath = os.path.dirname( os.path.abspath("__file__"))
print currentPath

# Make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv

# Open the file
csvFile = open(outputCsv, 'wb')
 

#  Result from above
#  C:\Users\Student\Documents\All My Essays\Python
#  C:\Users\Student\Documents\All My Essays\Python/ spreadsheet.csv
