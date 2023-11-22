#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
Session = sessionmaker(bind=engine)
session = Session()
all_states = session.query(State).order_by(State.id).all()
for state in all_states:
    print(f"{state.id}: {state.name}")
session.close()
