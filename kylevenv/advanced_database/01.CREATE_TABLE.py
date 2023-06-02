import sqlite3

conn = sqlite3.connect('D://python_basic/kylevenv/advanced_database/SQL_DDL.db')

cur = conn.cursor()

CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Item(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    )
"""

cur.execute(CREATE_SQL)

conn.close()