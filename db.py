import sqlite3
import random

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# cursor.execute("""
# # CREATE TABLE IF NOT EXISTS Users(
# # id INTEGER PRIMARY KEY,
# # username TEXT NOT NULL,
# # email TEXT NOT NULL,
# # age INTEGER
# # )
# # """)
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

cursor.execute("CREATE TABLES IF NOT EXISTS Users(
               id
               )



connection.commit()
connection.close()
