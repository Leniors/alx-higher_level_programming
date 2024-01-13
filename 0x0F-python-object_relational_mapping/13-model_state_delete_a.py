#!/usr/bin/python3
"""Delete states
"""
import sys
from model_state import Base, State
from sqlalchemy import delete, create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Execute when called"""
    engine = create_engine(
            f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    delete_statement = delete(State).where(State.name.like('%a%'))
    session.execute(delete_statement)
    session.commit()
    session.close()
