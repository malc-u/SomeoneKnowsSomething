import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, AddForm
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
      flash(f'Your account has been created.', 'primary')
      return redirect(url_for('index'))
      
    else:
      flash(f'Username already taken. Please try another one.', 'primary')
      return redirect(url_for('register'))

  return render_template('register.html', title='Register',
                           form=form_register)

@app.route('/logut')
def logout():
  session.clear()
  return render_template('index.html')

@app.route('/recommended')
def recommended():
  return render_template('recommended.html', 
  podcasts = mongo.db.podcasts.find({"is_recommended": True}))

@app.route('/favourites')
def favourites():
  return render_template('favourites.html', 
  podcasts = mongo.db.podcasts.find({"is_favourite": True}))

@app.route('/british')
def british():
  return render_template('origin.html', 
  podcasts = mongo.db.podcasts.find({"origin": 1}),
  origin = 'United Kingdom')

@app.route('/australian')
def australian():
  return render_template('origin.html', 
  podcasts = mongo.db.podcasts.find({"origin": 2}),
  origin = 'Australia')

@app.route('/american')
def american():
  return render_template('origin.html', 
  podcasts = mongo.db.podcasts.find({"origin": 3}),
  origin = 'USA')

@app.route('/read_more')
def read_more():
  return

@app.route('/your_account')
def your_account():
  current_user = session['username']
  return render_template('account.html', 
  podcasts = mongo.db.podcasts.find({"username": current_user}))

@app.route('/add_podcast', methods=['GET', 'POST'])
def add_podcast():
    add_form = AddForm()

    if request.method == 'POST':
        mongo.db.podcasts.insert_one({
            'username': session['username'],
            'podcast_title': add_form.podcast_title.data,
            'podcast_imgurl': add_form.podcast_imgurl.data,
            'origin': add_form.origin.data,
            'release_year': add_form.release_year.data,
            'description': add_form.description.data,
            'is_favourite': add_form.is_favourite.data,
            'is_recommended': False,
            'no_episodes': add_form.no_episodes.data,
            'podcast_link': add_form.podcast_link.data,
                    })
        flash(f'Your podcasts has been added', 'success')
        return redirect(url_for('your_account', title='Podcast Added'))

    return render_template('add_podcast.html', form=add_form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)
