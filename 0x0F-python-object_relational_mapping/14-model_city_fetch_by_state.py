#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    rows = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()
    for c, s in rows:
        print(f"{s.name}: ({c.id}) {c.name}")
