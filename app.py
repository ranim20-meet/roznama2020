#from database import *
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'greenwallx4@gmail.com'
app.config['MAIL_PASSWORD'] = 'funwithmeet19'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	return render_template('signup.html')

@app.route('/signin'. methods = ['GET', 'POST'])
def signin():
	return render_template('sign_in.html')

if __name__ == '__main__':
	app.run(debug=True)