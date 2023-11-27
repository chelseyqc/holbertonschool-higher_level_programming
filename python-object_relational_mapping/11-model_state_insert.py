#!/usr/bin/python3
"""Adds the State object Louisiana to the database hbtn_0e_6_usa"""
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    result = session.query(State).filter(State.name == "Louisiana")\
        .order_by(State.id.desc()).first()

    if result:
        print(result.id)
    session.commit()
    session.close()
