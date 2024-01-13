#!/usr/bin/python3
"""States with letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """only when called"""
    if len(sys.argv) != 4:
        sys.exit()
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    for state in states_with_a:
        print(f"{state.id}: {state.name}")
