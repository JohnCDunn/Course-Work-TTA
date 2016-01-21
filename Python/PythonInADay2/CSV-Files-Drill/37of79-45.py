
import sqlite3

conn = sqlite3.connect('simpsons.db')

def createTable():
    conn.execute("create tableif not exists simpson_info(ID Integet primary key autoincrement, \
                 Name text, Gender text, Age text, Occupationm text);")

    createTable()

# Results:
#
