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
    new_data = session.query(State).get(2)  # get the primary key element

    new_data.name = 'New Mexico'
    session.add(new_data)
    session.commit()

    session.close()


if __name__ == "__main__":
    main(sys.argv)
