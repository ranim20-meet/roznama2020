from database import *
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
# from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'greenwallx4@gmail.com'
app.config['MAIL_PASSWORD'] = 'funwithmeet19'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signup', methods=['POST'])
def signup():
	if request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		username = request.form['username']
		password = request.form['password']
		email_adr = request.form['email']
		add_user(first_name = first_name, last_name = last_name, username = username, password = password, email_adr = email_adr)
	return render_template('sign_in.html')

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
	if request.method == 'POST':
		user = get_user_by_username(request.form['username'])
		print(user)
		if user and user.verify_password(request.form['password']):
			login_session['name'] = user.username
			login_session['logged_in'] = True
			return redirect('/todo/user/'+user.username)
		else:
			print("false inp")
	return render_template('sign_in.html')

@app.route('/todo/user/<string:username>', methods = ['GET', 'POST'])
def todo(username):
	print(username)
	if (login_session['logged_in'] == False):
		return render_template('sign_in.html')
	else:
		user = get_user_by_username(login_session['name'])
		if request.method == 'POST':
			item_title = request.form['title']
			item_urgency = request.form['urgency']
			parent_username = username
			add_todo_item(parent_username = parent_username, item_title = item_title, item_urgency = item_urgency)
		todo_items = get_items_by_user_username(user.username)
		return render_template('to_do.html', user=user, todo_items=todo_items)

@app.route('/delete/<int:item_id>', methods = ['POST'])
def delete_item(item_id):
	delete_item_by_item_id(item_id)
	return redirect('/todo/user/'+login_session['name'])

@app.route('/mental-health', methods=['GET', 'POST'])
def mhealth():
    return render_template('mental_health_sources.html')

@app.route('/about-us', methods=['GET', 'POST'])
def about():
    return render_template('about_us.html')

if __name__ == '__main__':
	app.run(debug=True)