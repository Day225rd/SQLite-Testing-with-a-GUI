import sqlite3

def populate_table():
    connection = sqlite3.connect("1database.db")
    cursor = connection.cursor()

    users = [
        ("Kyle", 000-000-0000, "KyleJackson@mail.com", "WOWOWOWOWOWOW")
    ]