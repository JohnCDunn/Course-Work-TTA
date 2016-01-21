
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

newCharacter()



# Results:
#
#
#Adding a new character...
#Name: Bart
#Gender: male
#Age: 10
#Occupation: student
#'Bart', 'male',10, 'student'
