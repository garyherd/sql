# Update two records in inventory table
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    try:
        c.execute("UPDATE inventory SET Quantity = 17000 WHERE Model='Mustang'")
        c.execute("UPDATE inventory SET Quantity = 87000 WHERE Model='CRX'")
    except sqlite3.OperationalError as e:
        print "Something went wrong. Try again."
        print e.args

    print "New Data:\n"
    print "Make", "Model", "Qty\n"

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()

    for r in rows:
        print r[0], r[1], r[2]


