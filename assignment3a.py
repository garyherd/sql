import sqlite3
import random

rn_list = []

for i in range(1, 101):
    rn_list.append((random.randint(1, 100), ))

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers (num int)")
    c.executemany("INSERT INTO numbers VALUES(?)", rn_list)

