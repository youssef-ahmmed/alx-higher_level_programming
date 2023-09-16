#!/usr/bin/python3
"""script that changes the name of a State object from
the database hbtn_0e_6_usa"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1],
                                                         sys.argv[2],
                                                         sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.id == 2)\
                        .update({State.name: "New Mexico"})
    session.commit()

    session.close()
