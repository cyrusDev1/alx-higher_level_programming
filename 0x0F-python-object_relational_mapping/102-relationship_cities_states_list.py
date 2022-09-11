#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    for state, city in session.query(State, City).filter(
                                    City.state_id == State.id).all():
        print(f"{city.id}: {city.name} -> {state.name}")
    session.close()
