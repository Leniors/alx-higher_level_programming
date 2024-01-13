#!/usr/bin/python3
"""First state
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
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
