
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	username = Column(String)
	password_hash = Column(String)
	email_adr = Column(String)

	def hash_password(self, password):
		self.password_hash = pwd_security.encrypt(password)

	def verify_password(self, password):
		return pwd_security.verify(password, self.password_hash) 
	
	def __repr__(self):
		return("id: {}\n"
				"First Name: {}\n"
				"Last Name: {}\n"
				"Username: {}\n"
				"password_hash: {}\n"
				"Email: {}\n").format(
					self.user_id,
					self.first_name,
					self.last_name,
					self.username,
					self.password_hash,
					self.email_adr)


class Todo(Base):
	__tablename__ = 'todo_list'
	item_id = Column(Integer, primary_key=True)
	parent_username = Column(String)
	item_title = Column(String)
	item_urgency = Column(String)

	def __repr__(self):
		return ("id: {}\n"
				"Parent username: {}\n"
				"Item title: {}\n"
				"Item urgency: {}\n").format(
					self.item_id,
					self.parent_username,
					self.item_title,
					self.item_urgency)


