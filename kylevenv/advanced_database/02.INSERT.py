import sqlite3

conn = sqlite3.connect('D://python_basic/kylevenv/advanced_database/SQL_DDL.db')

cur = conn.cursor()

INSERT_SQL = "INSERT INTO item(code, name, price) VALUES (?, ?, ?)"

# Insert multiple data
data = (
    ('A00002', '에어컨', 350000),
    ('A00003', '스마트폰', 800000),
    ('A00004', '노트북', 350000)
)

cur.execute(INSERT_SQL, ('A00001', '게이밍 마우스', 38000))

cur.executemany(INSERT_SQL, data)

# 커밋 : INSERT, UPDATE, DELETE require commit
conn.commit()

conn.close()