import sqlite3

conn = sqlite3.connect('D://python_basic/kylevenv/advanced_database/SQL_DDL.db')

cur = conn.cursor()

SELECT_SQL = "SELECT * FROM item"

cur.execute(SELECT_SQL)

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()