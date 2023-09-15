#!/usr/bin/python3
"""List all states that starts with Upper `N` in the dataBase
"""


import MySQLdb
import sys


def main(av):
    """main function
    """
    dbconnect = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                                passwd=av[2], db=av[3])
    cursor = dbconnect.cursor()
    query = """
    SELECT id, name
    FROM states
    WHERE name LIKE 'N%'
    ORDER BY id ASC;
    """

    try:
        cursor.execute(query)
        query_rows = cursor.fetchall()
    except MySQLdb.Error as e:
        dbconnect.close()
        sys.exit(1)

    for row in query_rows:
        print(row)

    cursor.close()
    dbconnect.close()


if __name__ == "__main__":
    main(sys.argv)
