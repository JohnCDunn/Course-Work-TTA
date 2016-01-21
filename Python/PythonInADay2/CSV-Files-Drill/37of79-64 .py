
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

    sql_str = "insert into simpson_info \
              (name, gender, age, occupation) \
              values ({});".format(val_str)

    conn.execute(sql_str)
    conn.commit()

def printData(data):

    for row in data:
        print '\n'
        print "Id:", row[0]
        print "Name: ", row[1]
        print "Gender: ", row[2]
        print "Age: ", row[3]
        print "Occupation: ", row[4]
        
def viewAll():

    print 'Viewing all character details'
    sql_str = "select * from simpson_info"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    
    print printData(rows)

     
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
        change_id = row[0]
        printData(rows)
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input('Type the ID of the character to update: ')

    print "Change ID: ", change_id

    delete=raw_input("Confirm character delete (y/n): ")

    if delete == 'y':
        sql_str = "delete from simpson_info where ID={}".format(change_id)
        conn.execute(sql_str)
        conn.commit()
        print 'number of changes: ', conn.total_changes

def options():
    print '\nWhat would you like to do?'
    print '1. Add a new character'
    print '2. View all characters'
    print '3. Search for a character'
    print '4. Delete a character'
    print '5. Exit'

    response = raw_input('Enter number: ')
    
    if response == '1':
        newCharacter()
    elif response == '2':
        viewAll()
    elif response == '3':
        viewDetails()
    elif response == '4':
        deleteCharacter()
    else:
        print 'Exiting the program'
        return

def mainLoop():
    in_loop = True
    while in_loop = True:
        options()
        again = raw_input('Would you like to do something else? (y/n)')
        if again != 'y':
            in_loop = False
    

#viewDetails()
#deleteCharacter()
#options()
mainLoop()
