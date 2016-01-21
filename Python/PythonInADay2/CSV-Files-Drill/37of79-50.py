
import sqlite3

conn = sqlite3.connect('simpsons.db')

def createTable():
    conn.execute("create table if not exists simpson_info(ID Integer primary key autoincrement, \
                 Name text, Gender text, Age text, Occupation text);")

createTable() 
    

def newCharacter():
    print '\nAdding a new character...'

    name = raw_input("Name: ")
    gender = raw_input("Gender: ")
    age = raw_input("Age: ")
    occupation = raw_input("Occupation: ")
    val_str = "'{}', '{}',{}, '{}'".format(name, gender, age, occupation)
    print val_str
    sql_str = "insert into simpson_info \
              (name, gender, age, occupation) \
              values ({});".format(val_str)
    print sql_str
    conn.execute(sql_str)
    conn.commit()
    print "Number of changes: ", conn.total_changes

def viewAll():
    sql_str = "select * from simpson_info"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    print rows
    
viewAll()



# Results:
#
# [(1, u'Bart Simpson', u'Male', u'10', u'Student')]
