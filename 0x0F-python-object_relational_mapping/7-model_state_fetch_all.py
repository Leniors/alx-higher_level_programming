#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:root@localhost/hbtn_0e_6_usa')
Session = sessionmaker(bind=engine)
session = Session()
all_states = session.query(State).order_by(State.id).all()
for state in all_states:
    print(f"{state.id}: {state.name}")
session.close()
