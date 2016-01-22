import sqlite3
rosterValues = (

('Jean-Baptiste Zorg', 'Human', 122),
('Korben Dallas', 'Meat Puppet', 100),
("Ak'not", 'Mangalore', -5)

)

with sqlite3.connect('test_database.db') as connection:

    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues)
# update Korban to 'Human'
    c.execute("UPDATE Roster SET Species='Human' where Name='Korben Dallas'")


# select all Human Names and IQ

    c.execute("SELECT Name, IQ FROM Roster where Species == 'Human'")
    for row in c.fetchall():

        print row


#  Results from above
#  (u'Jean-Baptiste Zorg', 122)
#  (u'Korben Dallas', 100)

