
import sqlite3

conn = sqlite3.connect('simpsons.db')

cursor = conn.execute("Select integerprimary, name, gender, age, occupation from simpson_info")

print cursor

# Results:
#<sqlite3.Cursor object at 0x016B9AE0>
