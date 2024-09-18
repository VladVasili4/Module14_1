import sqlite3
import random

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLES IF NOT EXISTS Users(
id INT
username TEXT
first_name TEXT
block INT)""")

def aser_add():
    pass


connection.commit()
connection.close()
