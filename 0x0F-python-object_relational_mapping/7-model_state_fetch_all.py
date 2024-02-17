#!/usr/bin/python3
"""Start link class to table in database
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
    new_session = Session()
    for instance in new_session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
