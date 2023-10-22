#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Database connection details."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Create a connection to the database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    """ Create a session."""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query for the first State object ordered by states.id."""
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
