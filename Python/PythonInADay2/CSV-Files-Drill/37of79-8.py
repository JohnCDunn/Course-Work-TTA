import os, csv
# The path to the script
currentPath = os.path.dirname( os.path.abspath("__file__"))
print currentPath

# Make the spreadsheet path
outputCsv = currentPath + '/spreadsheet.csv'
print outputCsv

# Open the file
csvFile = open(outputCsv, "wb")

# Create writer object
writer = csv.writer(csvFile, delimiter=',')

# data to go into csv
row_1 = [1, "Row 1", 123]
row_2 = [2, "Row 2", 456]
row_3 = [3, "Row 3", 789]
rows = [row_1, row_2, row_3]

#  loop through rows and write them
for row in rows:
    writer.writerow(row)


#  Result from above
#  C:\Users\Student\Documents\All My Essays\Python
#  C:\Users\Student\Documents\All My Essays\Python/spreadsheet.csv

# on spreadsheet
#1  Row_1  123
#2  Row_2  456
#3  Row_3  789
