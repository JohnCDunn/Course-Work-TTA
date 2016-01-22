import sqlite3



conn = sqlite3.connect('time_database.db')

c = conn.cursor()

c.execute('''CREATE TABLE time_table (last_update text)''')

c.execute("INSERT INTO time_table VALUES ('20150101010101')")

conn.commit()

conn.close()

