import sqlite3

dbname = 'kibaco2.sqlite3'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

ID = input("Enter ID (ex: E00001): ")
name = input("Enter name (ex: 田中 太郎): ")
address = input("Enter address (ex: 東京都日野市): ")

cur.execute('INSERT INTO student (ID, name, address) VALUES (?, ?, ?)', (ID, name, address))

conn.commit()
conn.close()