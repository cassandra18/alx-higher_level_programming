#!/usr/bin/python3
"""Module contains a script that prints the states with letter 'a' in it."""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Connect to the database."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """Create a session to query the database."""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query the State objets containing letter 'a'."""
    result = session.query(State).filter(State.name.like('%a%'))
    result_order = result.order_by(State.id).all()

    """Print the results."""
    for state in result_order:
        print("{}: {}".format(state.id, state.name))

    session.close()
