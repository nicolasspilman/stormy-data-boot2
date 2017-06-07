#!/usr/bin/env python

from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String,DateTime,Text
from sqlalchemy.ext.declarative import declarative_base
import csv
import dateutil.parser as date_parser

engine = create_engine('postgresql://postgres:password@192.168.99.100:5432/boot2')

Session = sessionmaker(bind=engine)

Base = declarative_base()

class State(Base):
    __tablename__ = 'state'
    
    id = Column(Integer, primary_key=True)
    name=Column(String)
    
class StormType(Base):
    __tablename__ = 'storm_type'

    
    id = Column(Integer, primary_key=True)
    name=Column(String)

    


class StormInfo(Base):

    __tablename__ = 'storm_info'

    id = Column(Integer, primary_key=True)

    beginTimestamp = Column(DateTime)
    endTimestamp = Column(DateTime)
    state_id=Column(Integer,ForeignKey('state.id'))
    storm_type_id=Column(Integer,ForeignKey('storm_type.id'))
    comments =Column(Text)

def get_or_create(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()

    if not instance:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()

    return instance
    
if __name__=='__main__':

   storms = csv.DictReader(open("./stormdata_2013.csv"))

   Base.metadata.create_all(engine)

   session=Session()

   for storm in storms:

       state = get_or_create(session,State,name=storm['STATE'])
       storm_type=get_or_create(session,StormType,name=storm['EVENT_TYPE'])
       
       storm_info = StormInfo(beginTimestamp=date_parser.parse(storm['BEGIN_DATE_TIME']),
                              endTimestamp=date_parser.parse(storm['END_DATE_TIME']),
                              comments=storm["EPISODE_NARRATIVE"],
                              state_id=state.id,
                              storm_type_id=storm_type.id
       )
       
       
       session.add(storm_info)

   session.commit()
       


