#!/usr/bin/python3

# This module contains a script that lists all states.
# The name of the state must start with a upper N from db hbtn_0e_0_usa.

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

        
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

        executed_states = cursor.fetchall()

        for row in executed_states:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {e}".format(e))

    finally:
        cursor.close()
        db.close()
