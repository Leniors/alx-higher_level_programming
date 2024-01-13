#!/usr/bin/python3
"""Print cities
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """Execute when called"""
    engine = create_engine(
        f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()
