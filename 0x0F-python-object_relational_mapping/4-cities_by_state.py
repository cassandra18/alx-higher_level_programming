#!/usr/bin/python3

# This module contains a script that lists all cities from the DB


import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.agrv[1], sys.agrv[2], sys.agrv[3]

    try:
        db = MySQLdb.connect(
                host="localhots",
                user=username,
                passwd=password,
                db=database,
                port=3306
                )

        cursor = db.cursor()

        query = """
        SELECT  cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
        """

        cursor.execute(query)

        executed_states = cursor.fetchall()

        for row in executed_states:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        cursor.close()
        db.close()
