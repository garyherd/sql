# INSERT five rows of data into the inventory table of cars database
import sqlite3

car_data = [
    ('Ford', 'Mustange', 14000),
    ('Ford', 'F150', 100000),
    ('Ford', 'Fiesta', 1000),
    ('Honda', 'Civic', 1500500),
    ('Honda', 'CRX', 75000)
]

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    try:
        c.executemany("INSERT INTO inventory (?, ?, ?)", car_data)
    except sqlite3.OperationalError as e:
        print "Something went wrong, try again"
        print e.args

