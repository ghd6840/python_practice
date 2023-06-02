import sqlite3

conn = sqlite3.connect('D://python_basic/kylevenv/advanced_database/SQL_DDL.db')

cur = conn.cursor()

UPDATE_SQL = "UPDATE Item set price = 650000 WHERE code='A00002';"

cur.execute(UPDATE_SQL)

conn.commit()

conn.close()