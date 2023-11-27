#!/usr/bin/python3
"""Changes the name of a State object fromt the database htbn_0e_6_usa"""
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

    state_id_to_edit = 2
    state_to_edit = session.query(State).filter(State.id == state_id_to_edit)\
        .first()

    if state_to_edit:
        state_to_edit.name = "New Mexico"
    session.commit()
    session.close()
