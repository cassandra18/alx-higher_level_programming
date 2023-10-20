#!/usr/bin/python3

#0-select_states module contains a script that lists all USA states in the DB.
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                passwd=password,
                db=database,
                port=3306
                )

        # Create a cursor o interact with the database
        cursor = db.cursor()

        # Execute the query to select all states and order them by id
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all the results and print them
        selected_states = cursor.fetchall()

        for row in selected_states:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        # Close the cursor and the database connection
        cursor.close()
        db.close()
