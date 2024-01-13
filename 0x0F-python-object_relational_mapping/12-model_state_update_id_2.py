#!/usr/bin/python3
"""Updating a state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """only execute called"""
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    update_statement = update(State).where(
        State.id == 2).values(
        name='New Mexico')
    session.execute(update_statement)
    session.commit()
    session.close()
