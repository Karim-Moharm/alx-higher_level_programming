#!/usr/bin/python3
"""List all cities from database hbtn_0e_4_usa
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
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.state_id ASC;
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
