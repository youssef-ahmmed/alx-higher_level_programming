#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_u"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':

    db_url = f"""
        mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}
    """
    engine = create_engine(db_url)

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for instance in results:
        print(f'{instance.id}: {instance.name}')
