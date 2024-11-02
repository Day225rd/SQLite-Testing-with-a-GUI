import sqlite3
connection = sqlite3.connect('1database.db')
cursor = connection.cursor()

cursor.execute ('''DELETE FROM feedback WHERE name = ?''',('rserfs,	esfesfes, efsefs, 23232',))