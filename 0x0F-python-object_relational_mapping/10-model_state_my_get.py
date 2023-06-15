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

    state_filtered = session.query(State).filter(
            State.name.like("{}".format(sys.argv[4]))).all()
    if not state_filtered:
        print("Not found")
    else:
        print("{}".format(state_filtered[0].id))
    session.close()
