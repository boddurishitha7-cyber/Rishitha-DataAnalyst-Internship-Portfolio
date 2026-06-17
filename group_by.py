import sqlite3

conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

cursor.execute("""
SELECT Category, SUM(Sales)
FROM superstore
GROUP BY Category
""")

for row in cursor.fetchall():
    print(row)

conn.close()