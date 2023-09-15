#!/usr/bin/python3
"""List all states that starts with Upper `N` in the dataBase
"""


import MySQLdb


def main(av):
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                                passwd=av[2], db=av[3])
    cursor = dbconnect.cursor()
    query = "SELECT id, name\
            FROM states\
            ORDER BY id ASC\
            WHERE name LIKE 'A%';"

    cursor.execute(query)
    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    dbconnect.close()


if __name__ == "__main__":
    from sys import argv
    main(argv)
