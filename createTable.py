import sqlite3
connection = sqlite3.connect('newDB.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Feedback
               
               (name TEXT PRIMARY KEY
               , 
               number INT
               , 
               email TEXT
               , 
               feedback TEXT)
               ''')
cursor.commit()

#cursor.execute('''INSERT INTO Feedback VALUES
#               ('Kyle', '000-000-0000', '@mail.com', 'L database')''' )

#cursor.execute("SELECT * FROM feedback")
#print(cursor.fetchall())