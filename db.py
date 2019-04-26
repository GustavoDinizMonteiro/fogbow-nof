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

    def __str__(self):
        return "Member {} with id: {} has justice: {} and quota: {}".format(
            self.member, self.id, self.justice, self.quota
        )

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

def create_member(member_name, justice=1):
    member = Fairness(member=member_name, justice=justice)
    session.add(member)
    session.commit()
    return member


def update_global(justice = 1): # TODO: check how is the default value for this.
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

def get_member_data(member_name):
    members = session.query(Fairness)
    for member in members:
        if member.member == member_name:
            return member
    return create_member(member_name)

__ALL__ = [create_member, update_global, get_members_data, get_member_data]