import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
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

@app.route('/login', methods=['GET', 'POST'])
def login():

  form_login = LoginForm()

  if form_login.validate_on_submit():
    existing_user = mongo.db.users.find_one({'username': form_login.username.data})
    
    if not existing_user:
      flash(f'Username not found. Please try again or register.', 'warning')
      return redirect(url_for('register'))

    elif existing_user is not None and check_password_hash(existing_user['password'], form_login.password.data):
      session['username'] = request.form.get('username')
      return redirect(url_for('index'))
    
    flash(f'Password incorrect. Please try again.', 'success')
    return redirect(url_for('login'))

  return render_template('login.html', title = 'Login', form = form_login ) 

@app.route('/register', methods=['GET', 'POST'])
def register():
  form_register = RegistrationForm()

  if form_register.validate_on_submit():
    existing_username = mongo.db.users.find_one({'username': request.form['username']})
 
    if not existing_username:
      entered_password = request.form['password']
      password_hashed = generate_password_hash(entered_password)
      mongo.db.users.insert({'username': form_register.username.data,
                                    'password': password_hashed})
      session['username'] = request.form.get('username')
      flash(f'Your account has been created. Please log in.', 'primary')
      return redirect(url_for('index'))
      
    else:
      flash(f'Username already taken. Please try another one.', 'primary')
      return redirect(url_for('register'))

  return render_template('register.html', title='Register',
                           form=form_register)

@app.route('/logut')
def logout():
  return render_template('index.html')

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
