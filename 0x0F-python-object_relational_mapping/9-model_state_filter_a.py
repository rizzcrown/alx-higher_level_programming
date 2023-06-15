#!/usr/bin/python3
"""script that prints the first state from
the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """main function"""
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, db))

    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
