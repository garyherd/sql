import sqlite3

selection = ""

sql_dict = {'1': ("Average", "SELECT avg(num) FROM numbers"),
            '2': ("Maximum", "SELECT max(num) FROM numbers"),
            '3': ("Minimum", "SELECT min(num) FROM numbers"),
            '4': ("Sum", "SELECT sum(num) FROM numbers")}


while True:
    print "Select an operation:"
    selection = raw_input("1: AVG, 2: MAX, 3: MIN, 4: SUM, 5: EXIT>>")

    if selection == '5':
        print "Goodbye"
        exit()

    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()
        c.execute(sql_dict[selection][1])

        result = c.fetchone()

        print "{} is: {}".format(sql_dict[selection][0], result[0])



