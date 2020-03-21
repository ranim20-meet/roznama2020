from database import *
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
# from flask_mail import Mail, Message

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'you-will-never-guess'
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'greenwallx4@gmail.com'
# app.config['MAIL_PASSWORD'] = 'funwithmeet19'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		first_name = request.form['first_name']
		last_name = request.form['last_name']
		username = request.form['username']
		password = request.form['password']
		email_adr = request.form['email']
		add_user(first_name = first_name, last_name = last_name, username = username, password = password, email_adr = email_adr)
		user = get_user_by_username(username)
		login_session['name'] = user.username
		login_session['logged_in'] = True
		return render_template("home.html")
	return render_template('signup.html')

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
	if request.method == 'POST':
		user = get_user_by_username(request.form['username'])
		print(user)
		if user and user.verify_password(request.form['password']):
			login_session['name'] = user.username
			login_session['logged_in'] = True
			return render_template('home.html')
		else:
			print("false inp")
	return render_template('sign_in.html')

if __name__ == '__main__':
	app.run(debug=True)