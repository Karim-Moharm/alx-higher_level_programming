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
    WHERE BINARY name='{}'
    """.format(av[4])

    try:
        cursor.execute(query)
        query_rows = cursor.fetchall()
    except MySQLdb.Error as e:
        dbconnect.close()
        sys.exit(1)

    for row in query_rows:
        # if row[1] == av[4]:
        print(row[1])

    cursor.close()
    dbconnect.close()


if __name__ == "__main__":
    main(sys.argv)
