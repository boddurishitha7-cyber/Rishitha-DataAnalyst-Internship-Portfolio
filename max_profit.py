import sqlite3

conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

cursor.execute("""
SELECT "Customer_Name", MAX(Profit)
FROM superstore
""")

print(cursor.fetchone())

conn.close()