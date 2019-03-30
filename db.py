import os
from dotenv import load_dotenv
from sqlalchemy import create_engine  
from sqlalchemy import Column, Integer, String  
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base  

load_dotenv()

DB_HOST = os.getenv('DB_HOST')

db = create_engine(DB_HOST)
base = declarative_base()

class Fairness(base):
    __tablename__ = 'fairness'

    id = Column(Integer, primary_key=True)
    member = Column(String, nullable=False)
    justice = Column(Integer, nullable=False)
    quota = Column(Integer)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

def create_member(member_name, justice=1):
    member = Fairness(member=member_name, justice=justice)
    session.add(member)
    session.commit()


def update_global(justice):
    members = session.query(Fairness)
    for member in members:
        if member.member == 'global':
            member.justice = justice
            session.commit()
            return None
    global_fairness = Fairness(member='global', justice=justice)
    session.commit()

def get_members_data():
    return session.query(Fairness)

def get_member_data(member):
    members = session.query(Fairness)
    for member in members:
        if member.member == member:
            return member

__ALL__ = [create_member, update_global, get_members_data, get_member_data]