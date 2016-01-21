
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

def deleteCharacter():

    print 'Deleting a character'

    name = raw_input("Enter the character's name: ")

    sql_str = "select * from simpson_info \
              where name ='{}'".format(name)

    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    change_id = 0
    
    if len(rows) == 0:
        print "no records found"
        return
    elif len(rows) == 1:
        print 'One record found'
        row = rows[0]
        change_id = rows[0]
        printData(rows)
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input('Type the ID of the character to update: ')

    print "Change ID: ", change_id

#viewDetails()
deleteCharacter()

# Results:
#
#Viewing character details
#Enter the character's name: John
#no records found
