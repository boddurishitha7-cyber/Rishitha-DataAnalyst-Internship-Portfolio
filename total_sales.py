import sqlite3

conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

cursor.execute("SELECT SUM(Sales) FROM superstore")
print(cursor.fetchone()[0])

conn.close()