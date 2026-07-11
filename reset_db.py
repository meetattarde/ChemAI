import sqlite3

conn = sqlite3.connect("data/chemai.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM compounds")

conn.commit()
conn.close()

print("Database cache cleared.")