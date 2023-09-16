#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
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

    query = session.query(State).filter(State.name == av[4]).\
            order_by(State.id)

    if query is None:
        print('Not found')
    else:
        print("{}".format(query[0].id))

    session.close()


if __name__ == "__main__":
    main(sys.argv)
