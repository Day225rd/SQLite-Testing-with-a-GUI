import sqlite3
connection = sqlite3.connect('1database.db')
cursor = connection.cursor()

cursor.execute('''DELETE FROM <tablename> WHERE <columnName> =''' )