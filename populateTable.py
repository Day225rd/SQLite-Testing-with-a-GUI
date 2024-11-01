import sqlite3
connection = sqlite3.connect('1database.db')
cursor = connection.cursor()

cursor.execute('''INSERT INTO Feedback VALUES
               ('Kyle', '000-000-0000', '@mail.com', 'L database')''' )