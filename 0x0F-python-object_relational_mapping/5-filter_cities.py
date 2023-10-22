#!/usr/bin/python3

""" Script that takes in the name of a state as an argument.
    List all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQL.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
            )

    cursor = db.cursor()

    query = """
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """

    cursor.execute(query, (state_name,))

    executed_state = cursor.fetchone()

    if executed_state and executed_state[0]:
        print(executed_state[0])
    else:
        print("No cities found for the specified state.")

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        cursor.close()
        db.close()
