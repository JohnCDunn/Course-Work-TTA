import os, csv
# The path to the script
currentPath = os.path.dirname( os.path.abspath("__file__"))
print currentPath

# Make the spreadsheet path
inputCsv = currentPath + '/spreadsheet.csv'
print inputCsv

# Open the file
csvFile = open(inputCsv, "rb")

# Create writer object
reader = csv.reader(csvFile, delimiter=',')

# Add data to array
readerData = []
for row in reader:
    readerData.append(row)

print readerData

#  Result from above
#  C:\Users\Student\Documents\All My Essays\Python
#  C:\Users\Student\Documents\All My Essays\Python/spreadsheet.csv
#  [['1', 'Row 1', '123'], ['2', 'Row 2', '456'], ['3', 'Row 3', '789']]


