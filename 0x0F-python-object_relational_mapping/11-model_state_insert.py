#!/usr/bin/python3
"""Add a state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """execute only when called"""
    if len(sys.argv) < 4:
        sys.exit()
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Session = sessionmaker(bind=engine)
    louisiana = State(name="Louisiana")
    session = Session()
    session.add(louisiana)
    louisiana_id = session.query(State).filter(
        State.name == "Louisiana").first()
    print(louisiana_id.id)
    session.commit()
    session.close()
