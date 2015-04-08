# Using the COUNT() function, calculate the total number of orders for each make and
# model.

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT make, model, count(order_date)
                FROM orders
                GROUP BY make, model""")

    rows = c.fetchall()

    print "{0:6}{1:7}{2:3}".format('Make', 'Model', 'Order Count')
    print "------------------------"
    for row in rows:
        print "{0:6}{1:7}{2:3}".format(row[0], row[1], row[2])
