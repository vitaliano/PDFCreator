import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE teste (id INTEGER PRIMARY KEY, nome TEXT)")
conn.commit()
conn.close()