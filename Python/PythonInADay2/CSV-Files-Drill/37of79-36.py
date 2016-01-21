
import sqlite3

conn = sqlite3.connect('simpsons.db')

changes=conn.total_changes

print "Number of changes: ", changes



#  Results
#  Number of changes:  0
