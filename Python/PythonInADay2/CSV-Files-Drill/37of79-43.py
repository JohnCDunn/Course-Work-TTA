
import sqlite3

conn = sqlite3.connect('simpsons.db')

conn.execute("DROP TABLE SIMPSON_INFO")

cursor = conn.execute("select * from simpson_info WHERE NAME='Homer Simpson'")

rows = cursor.fetchall()
print rows


# Results:
#OperationalError: no such table: simpson_info  -  expected
