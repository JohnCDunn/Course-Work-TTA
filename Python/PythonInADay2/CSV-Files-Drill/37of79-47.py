
import sqlite3

conn = sqlite3.connect('simpsons.db')

def createTable():
    conn.execute("create tableif not exists simpson_info(ID Integet primary key autoincrement, \
                 Name text, Gender text, Age text, Occupationm text);")

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
#insert into simpson_info
#(name, gender, age, occupation)
#values ('Bart Simpson', 'Male',10, 'Student');
