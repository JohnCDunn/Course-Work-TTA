
import sqlite3

conn = sqlite3.connect('simpsons.db')

cursor = conn.execute("Select * from simpson_info")

rows = cursor.fetchall()

print rows

# Results:
#[(1, u'Bart Simpson', u'Male', 10, u'Student'),
# (2, u'Homer Simpson', u'Male', 40, u'Nuclear Plant'),
# (3, u'Lisa Simpson', u'Female', 8, u'Student')]
