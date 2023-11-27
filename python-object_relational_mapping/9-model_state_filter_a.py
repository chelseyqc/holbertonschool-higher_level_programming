#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()

    result = session.query(State)\
        .order_by(State.id).filter(State.name.like('%a%'))

    for state in result:
        print("{}: {}".format(state.id, state.name))
    session.close()
