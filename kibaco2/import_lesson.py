import sqlite3

dbname = 'kibaco2.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

ID = input("Enter ID (ex: L0001): ")
name = input("Enter name (ex: 線形数学I): ")
teacher = input("Enter teacher (ex: 山田 太郎): ")

cur.execute('INSERT INTO lesson (ID, name, teacher) VALUES (?, ?, ?)', (ID, name, teacher))

conn.commit()
conn.close()