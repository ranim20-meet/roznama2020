from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class Users(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=true)
	username = Column(String)
	password_hash = Column(String)
	email_adr = Column(String)
	