import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("""SELECT Make, Model, count(OD) as Cnt, inv
                FROM
                (SELECT orders.make as Make,
                orders.model as Model,
                orders.order_date as OD,
                inventory.Quantity as inv FROM orders
                INNER JOIN inventory
                ON orders.model=inventory.model)
                GROUP BY Make, Model, inv""")
    results = c.fetchall()

    for result in results:
        print result[0], result[1]
        print result[3]
        print result[2]
        print ""