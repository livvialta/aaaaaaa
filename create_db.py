import sqlite3

# Connect to the database
conn = sqlite3.connect('expenses.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS expenses
(id INTEGER PRIMARY KEY,
Date DATE,
description TEXT,
category TEXT,
price REAL)""")

# confirme the changes in the db.
conn.commit()

# close conn.
conn.close()