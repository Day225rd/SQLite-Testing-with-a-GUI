import sqlite3
connection = sqlite3.connect('1database.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS feedback
               
               (Name TEXT PRIMARY KEY
               , 
               Number INT
               , 
               Email TEXT
               , 
               Feedback TEXT)
               ''')

#cursor.execute('''INSERT INTO Feedback VALUES
#               ('Kyle', '000-000-0000', '@mail.com', 'L database')''' )

#cursor.execute("SELECT * FROM feedback")
#print(cursor.fetchall())