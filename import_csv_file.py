# import from CSV

# import the csv library
import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    employees = csv.reader(open("employees2.csv", "rU"))

    # create a new table called employees
    # c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) VALUES(?, ?)", employees)
