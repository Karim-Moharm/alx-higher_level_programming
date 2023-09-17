#!/usr/bin/python3


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city impoer Base, City
import sys


def main(av):
    engine = create_engine(f'mysql+mysqldb://{av[1]}:{av[2]}@localhost:3306/
                            {av[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.close()


if __name__ == "__main__":
    main(sys.argv)
