#!/usr/bin/python3

# This module contains a script that takes in argument.
# It displays the values in the  states table of from db hbtn_0e_0_usa.
# Where name matches the argument.

import MySQLdb
import sys

if __name__ == "__main__":
    usernm, password, dtbase, st_name = sys.agrv[1], sys.agrv[2], sys.agrv[3]

    try:
        db = MySQLdb.connect(
                host="localhots",
                user=usernm,
                passwd=password,
                db=dtbase,
                port=3306
                )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id"
        query_format = query.format(st_name)
        cursor.execute(query_format)

        executed_states = cursor.fetchall()

        for row in executed_states:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        cursor.close()
        db.close()
