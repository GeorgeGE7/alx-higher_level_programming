#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr = sys.argv[1]
    pas = sys.argv[2]
    host="localhost"
    db=sys.argv[3]
    sql_engine = create_engine(f'mysql+mysqldb://{usr}:{pas}@{host}/{db}', pool_pre_ping=True)
    Base.metadata.create_all(sql_engine)
    Session = sessionmaker(bind=sql_engine)
    session = Session()
    instance = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
