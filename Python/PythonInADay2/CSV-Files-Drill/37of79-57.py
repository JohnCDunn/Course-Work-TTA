
import sqlite3

conn = sqlite3.connect('simpsons.db')

def createTable():

    conn.execute("create table if not exists simpson_info(ID Integer primary key autoincrement, \
                 Name text, Gender text, Age text, Occupation text);")

createTable() 
    
        
def newCharacter():


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

def viewAll():

    sql_str = "select * from simpson_info"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    
def printData(data):

    loopCnt = 0
    for row in data:
        print "Id:", row[0]
        print "Name: ", row[1]
        print "Gender: ", row[2]
        print "Age: ", row[3]
        print "Occupation: ", row[4]
     
def viewDetails():

    print 'Viewing character details'

    name = raw_input("Enter the character's name: ")

    sql_str = "select * from simpson_info \
              where name ='{}'".format(name)

    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    if len(rows) == 0:
        print "no records found"
    else:
        print printData(rows)


viewDetails()

# Results:
#
#Viewing character details
#Enter the character's name: John
#no records found
