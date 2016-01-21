
import sqlite3

conn = sqlite3.connect('simpsons.db')

conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) \
     VALUES ('Homer Simpson', 'Male', 40, 'Nuclear Plant')")
conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) \
     VALUES ('Lisa Simpson', 'Female', 8, 'Student')")
conn.commit()

# Results:
