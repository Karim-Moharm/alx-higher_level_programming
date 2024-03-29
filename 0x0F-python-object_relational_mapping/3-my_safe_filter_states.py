#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
table of hbtn_0e_0_u
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
    WHERE name=%s AND LENGTH(name) BETWEEN 3 AND 15
    ORDER BY id ASC;
    """

    try:
        cursor.execute(query, (av[4],))
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
