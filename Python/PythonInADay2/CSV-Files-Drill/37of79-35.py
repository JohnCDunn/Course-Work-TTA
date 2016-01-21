
import sqlite3

conn = sqlite3.connect('simpsons.db')

conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Bart Simpson', 'Male', 10, 'Student')")

conn.commit()
