#!/usr/bin/python3
"""lists first State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    if first:
        first = session.query(State).order_by(State.id).first()
    else:
        print("Nothing")
    print(f'{first.id}: {first.name}')
    session.close()
