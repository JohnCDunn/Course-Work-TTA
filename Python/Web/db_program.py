import sqlite3

# Connect to simpsons database
conn = sqlite3.connect('html.db')

def createTable():
    conn.execute("CREATE TABLE if not exists \
        HTML_INFO( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        TITLE TEXT, \
        BODY TEXT, \
        PARAGRAPH TEXT, \
        FOOTER TEXT \
        );")
    
def printData(data):
    for row in data:
        print ("Id:", row[0])
        print ("Title:", row[1])
        print ("Body:", row[2])
        print ("Paragraph:", row[3])
        print ("Footer:", row[4], "\n")

def newHTML(title,body,paragraph,footer):   
    # Create values part of sql command
   
    val_str = '"{}", "{}", "{}", "{}"'.format(\
        title, body, paragraph, footer)
    
    sql_str = "INSERT INTO HTML_INFO \
        (TITLE, BODY, PARAGRAPH, FOOTER) \
        VALUES ({});".format(val_str)

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes
    
def viewAll():
    # Create sql string
    sql_str = "SELECT * from HTML_INFO"
    cursor = conn.execute(sql_str)
    
    # Get data from cursor in array
    rows = cursor.fetchall()
    return rows

def updateHTML(change_id,title,body,paragraph,footer):
    # Create values part of sql command
    val_str = 'TITLE="{}", BODY="{}",\
              PARAGRAPH="{}", FOOTER="{}"'.format(\
              title, body, paragraph, footer)
    
    sql_str = "UPDATE HTML_INFO set \
       {} where ID={};".format(val_str,change_id)
    print sql_str
    
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def deleteHTML(change_id):
    # Create sql string
    sql_str = "DELETE from HTML_INFO where ID={}"\
             .format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

createTable()
