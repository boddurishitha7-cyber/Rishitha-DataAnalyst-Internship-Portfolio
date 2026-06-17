import sqlite3

conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM superstore WHERE Category='Technology'")
for row in cursor.fetchall():
    print(row)

conn.close()