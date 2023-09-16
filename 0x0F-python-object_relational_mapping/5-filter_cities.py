#!/usr/bin/python3
"""takes in the name of a state as an argument and
lists all cities of that state
using the database hbtn_0e_4_usa
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
        if row[2] == av[4]:
            print(row[1], end=', ')
    print()

    cursor.close()
    dbconnect.close()


if __name__ == "__main__":
    main(sys.argv)
