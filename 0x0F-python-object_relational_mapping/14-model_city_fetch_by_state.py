#!/usr/bin/python3


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


def main(av):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    av[1], av[2], av[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(City, State).filter(State.id == City.state_id).\
            order_by(City.state_id)

    for obj in objs:
        print(obj.name, obj.state_id, obj.id)

    session.close()


if __name__ == "__main__":
    main(sys.argv)
