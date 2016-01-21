
import sqlite3

conn = sqlite3.connect('simpsons.db')

conn.execute("DELETE from SIMPSON_INFO Where ID=5")

conn.commit()

changes = conn.total_changes
print "Number of changes: ", changes

cursor = conn.execute("select * from simpson_info")

rows = cursor.fetchall()
print rows


# Results:
#Number of changes:  1
#[(1, u'Bart Simpson', u'Male', u'Student', 10),
# (3, u'Homer Simpson', u'Male', u'Nuclear Plant', 40)]
