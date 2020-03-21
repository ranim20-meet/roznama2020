from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# START USER CODE

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(first_name, last_name, username, password, email_adr):
	"""
	Add  new user
	"""
	new_user = User(first_name = first_name, last_name = last_name, username = username, email_adr = email_adr)
	new_user.hash_password(password)
	session.add(new_user)
	session.commit()

def get_user_by_username(username):
	return session.query(User).filter_by(username = username).first()

def get_all_users():
	return session.query(User).all()

def get_all_emails():
	all_users =  get_all_users()
	emails = []
	for user in all_users:
		emails.append(user.email_adr)
	return emails
