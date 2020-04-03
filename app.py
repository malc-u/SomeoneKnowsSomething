import os
from flask import Flask, render_template, url_for, redirect, request, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from os import path


if path.exists("env.py"):
  import env
  
app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv("MONGO_DBNAME")
app.config['MONGO_URI'] = os.getenv("MONGODB_URI")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/register')
def register():
  form_register = RegistrationForm()
  return render_template('register.html', title = 'Register', form = form_register )

@app.route('/login')
def login():
  form_login = LoginForm()
  return render_template('login.html', title = 'Login', form = form_login )


@app.route('/recommended')
def recommended():
  return render_template('recommended.html', 
  podcasts = mongo.db.podcasts.find({"is_recommended": True}))

@app.route('/read_more')
def read_more():
  return

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)
