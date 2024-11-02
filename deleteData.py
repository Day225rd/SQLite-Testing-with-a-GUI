import sqlite3
connection = sqlite3.connect('newDB.db')
cursor = connection.cursor()


cursor.execute("DELETE FROM feedback WHERE Name = 'ww'")



connection.commit()
#WARNING
#WARNING
#WARNING
#WARNING
#WARNING WILL NUKE, TYPE IN EXACT WORDS