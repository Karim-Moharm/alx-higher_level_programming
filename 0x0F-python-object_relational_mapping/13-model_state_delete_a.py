#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def main(av):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    av[1], av[2], av[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    # creating an instance of Session class
    session = Session()

    rows = session.query(State).filter(State.name.like('%a%'))
    for row in rows:
        session.delete(row)
        session.commit()

    session.close()


if __name__ == "__main__":
    main(sys.argv)
