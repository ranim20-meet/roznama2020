from model import Base, User, Todo

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
	"""
	Get specific user by username
	"""
	return session.query(User).filter_by(username = username).first()

def get_all_users():
	"""
	Get all users
	"""
	return session.query(User).all()

def get_all_emails():
	"""
	Get all users' email addreses
	"""
	all_users =  get_all_users()
	emails = []
	for user in all_users:
		emails.append(user.email_adr)
	return emails


#END USER CODE
#-------------
#START TODO CODE

engine1 = create_engine('sqlite:///todo.db?check_same_thread=False')
Base.metadata.create_all(engine1)
DBSession1 = sessionmaker(bind=engine1)
session1 = DBSession1()

def add_todo_item(parent_username, item_title, item_urgency):
	new_item = Todo(parent_username = parent_username, item_title = item_title, item_urgency = item_urgency)
	session1.add(new_item)
	session1.commit()

def get_all_items():
	return session1.query(Todo).all()

def get_items_by_user_username(parent_username):
	items = get_all_items()
	to_return = []
	for item in items:
		if item.parent_username == parent_username:
			to_return.append(item)
	return to_return

def delete_item_by_item_id(item_id):
	session1.query(Todo).filter_by(item_id = item_id).delete()
	session1.commit()
