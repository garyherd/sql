# Create orders table, and add data

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

   # c.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)")

    order_data = [
        ('Ford', 'Mustang', '2014-01-05'),
        ('Ford', 'Mustang', '2014-02-05'),
        ('Ford', 'Mustang', '2014-03-05'),
        ('Ford', 'F150', '2013-05-15'),
        ('Ford', 'F150', '2013-06-15'),
        ('Ford', 'F150', '2013-07-15'),
        ('Ford', 'Fiesta', '2015-03-17'),
        ('Ford', 'Fiesta', '2015-03-18'),
        ('Ford', 'Fiesta', '2015-03-19'),
        ('Honda', 'Civic', '2012-12-01'),
        ('Honda', 'Civic', '2012-12-08'),
        ('Honda', 'Civic', '2012-12-15'),
        ('Honda', 'CRX', '2011-06-05'),
        ('Honda', 'CRX', '2011-07-05'),
        ('Honda', 'CRX', '2011-08-05'),
    ]

    # c.executemany("INSERT INTO orders VALUES (?, ?, ?)", order_data)

    c.execute("SELECT Make, Model, Quantity FROM inventory")

    models = c.fetchall()

    for model in models:
        c.execute("""SELECT inventory.Model, orders.order_date FROM inventory, orders
                    WHERE inventory.Model = orders.model and inventory.model='{}'""".format(model[1]))
        model_data = c.fetchall()
        print model[0], model[1]
        print model[2]
        for item in model_data:
            print item[1]
        print

