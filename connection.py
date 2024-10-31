import sqlite3
connection = sqlite3.connect('1database.db')
cursor = connection.cursor

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Feedback
               
               (Name TEXT
               , 
               Number INT
               , 
               Email TEXT
               , 
               Feedback TEXT)
               ''')

cursor.execute('SELECT * FROM Feedback')

cursor.ecxecute('''
                INSERT INTO Feedback VALUES
                ('Kyle', 
                000:000:0000, 
                'KyleJackson@mail.com, 
                'This database sucks')
                ''')