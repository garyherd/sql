# Output only records where Make = 'Ford'

import sqlite3

rows = []

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("SELECT * FROM inventory WHERE Make='Ford'")
    rows = c.fetchall()

for r in rows:
    print r[0], r[1], r[2]

