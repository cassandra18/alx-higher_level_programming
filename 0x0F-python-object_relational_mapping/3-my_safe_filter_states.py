#!/usr/bin/python3

# This module contains a script that takes in argument.
# It displays the values in the  states table of from db hbtn_0e_0_usa.
# Where name matches the argument.
# This methos is safer than usingg formating to create sql query.

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, searched_state = sys.agrv[1], sys.agrv[2], sys.agrv[3]

    try:
        db = MySQLdb.connect(
                host="localhots",
                user=username,
                passwd=password,
                db=database,
                port=3306
                )

        cursor = db.cursor()

        query = ("SELECT * FROM states WHERE name = %s ORDER BY id")
        cursor.execute(query, (searched_state,))

        executed_states = cursor.fetchall()

        for row in executed_states:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        cursor.close()
        db.close()
