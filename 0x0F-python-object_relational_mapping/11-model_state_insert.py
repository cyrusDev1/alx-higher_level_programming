#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the
database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)
    session.close()
