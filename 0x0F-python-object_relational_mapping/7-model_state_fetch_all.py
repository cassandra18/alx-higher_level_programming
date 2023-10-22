#!/usr/bin/python3
"""
This module contains a script that lists all State objects from the db.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Set up engine connection
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """ Create a ssession to interact with the database."""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query the States Objects and sort them by states.id."""
    states = session.query(State).order_by(State.id).all()

    """ Print the results."""
    for state in states:
        print("{}: {}".format(state.id, state.name))

    """ Close the session."""
    session.close()
