#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    usr=sys.argv[1]
    pas=sys.argv[2]
    db=sys.argv[3]
    host="localhost:3306"
    sql_engine = create_engine(f'mysql+mysqldb://{usr}:{pas}@{host}/{db}',
                           pool_pre_ping=True)
    Base.metadata.create_all(sql_engine)

    Session = sessionmaker(bind=sql_engine)
    new_session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    new_session.add(newState)
    new_session.add(newCity)
    new_session.commit()
