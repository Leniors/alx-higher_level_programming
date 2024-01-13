#!/usr/bin/python3
"""Find state
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """only when called"""
    if len(sys.argv) != 5:
        sys.exit()
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    search_name = sys.argv[4]
    state = session.query(State).filter(State.name == search_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")
