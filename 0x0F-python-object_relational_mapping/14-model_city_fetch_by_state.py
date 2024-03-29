#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


def main(av):
    """main function
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    av[1], av[2], av[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id)

    for state, city in objs:
        # print(state.name, city.state_id, city.name)
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    main(sys.argv)
