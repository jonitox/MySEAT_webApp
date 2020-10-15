from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Engine = create_engine('mysql://root:1234@localhost/example?charset=utf8',pool_recycle=3600)

Base = declarative_base()
Session = scoped_session(sessionmaker(autocommit=True,autoflush=True, bind=Engine))

class member(Base):
    ############ problem 1-(1) ############
    __tablename__="member"
    num = Column(Integer,primary_key=True)
    id = Column(String(100))
    password = Column(String(200))
    name = Column(String(45))
    nickname = Column(String(45))
    maxf=Column(Integer)
    #######################################
    
    def __repr__(self):
        return '<<<Member>>> ::: %s' %self.name


class tabledb(Base):
    ############ problem 1-(2) ############
    __tablename__="tabledb"
    num = Column(Integer,primary_key=True)
    id = Column(String(100))
    floor = Column(Integer)
    numx = Column(Integer)
    seatx = Column(Integer)
    seaty = Column(Integer)
    color = Column(String(45))
    info = Column(String(100))
	
	#######################################
    



Base.metadata.create_all(Engine)
