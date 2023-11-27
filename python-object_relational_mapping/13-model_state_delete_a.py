#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""
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

    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in state_to_delete:
        session.delete(state)
    session.commit()
    session.close()
