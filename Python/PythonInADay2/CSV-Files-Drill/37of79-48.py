
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

newCharacter()



# Results:
#
#
#Adding a new character...
#Name: Bart Simpson
#Gender: Male
#Age: 10
#Occupation: Student
#'Bart Simpson', 'Male',10, 'Student'
#insert into simpson_info               (name, gender, age, occupation)               values ('Bart Simpson', 'Male',10, 'Student');
#Number of changes:  1
#values ('Bart Simpson', 'Male',10, 'Student');
