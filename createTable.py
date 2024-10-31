import sqlite3
connection = sqlite3.connect('1database.db')
cursor = connection.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Feedback
               
               (Name TEXT PRIMARY KEY
               , 
               Number INT
               , 
               Email TEXT
               , 
               Feedback TEXT)
               ''')