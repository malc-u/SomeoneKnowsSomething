import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, AddForm, UpdateForm, DeleteForm
from bson.objectid import ObjectId
from os import path

if path.exists("env.py"):
  import env
  
app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

"""
Check_password_hash part is based on example no 9 from this page
https://www.programcreek.com/python/example/58659/werkzeug.security.check_password_hash
but it was amended and updated to suit the needs of this app
"""
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
  podcasts = mongo.db.podcasts.find({"is_recommended": True}), recommended = "Recommended")

@app.route('/favourites')
def favourites():
  return render_template('recommended.html', 
  podcasts = mongo.db.podcasts.find({"is_favourite": True}), recommended = "Users favourites")

@app.route('/british')
def british():
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
    return render_template('origin.html', 
    podcasts = mongo.db.podcasts.find({"origin": 1}),
    origin = 'United Kingdom')

@app.route('/australian')
def australian():
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
    return render_template('origin.html', 
    podcasts = mongo.db.podcasts.find({"origin": 2}),
    origin = 'Australia')

@app.route('/american')
def american():
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
    return render_template('origin.html', 
    podcasts = mongo.db.podcasts.find({"origin": 3}),
    origin = 'USA')

@app.route('/read_more/<podcast_id>', methods=['GET', 'POST'])
def read_more(podcast_id):
  picked_podcast = mongo.db.podcasts.find_one({'_id': ObjectId(podcast_id)})

  return render_template('read_more.html', podcast = picked_podcast)

@app.route('/your_account')
def your_account():
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
    current_user = session['username']
    return render_template('account.html', 
    podcasts = mongo.db.podcasts.find({"username": current_user}))
    


@app.route('/add_podcast', methods=['GET', 'POST'])
def add_podcast():
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
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
    
"""
Used request.method == 'GET' following advice from 
https://romain.dorgueil.net/wiki/python/wtforms and https://stackoverflow.com/a/23714791
to populate update form with existing in database details for the podcast that user 
wants to amend. 
"""
@app.route('/update_podcast/<podcast_id>', methods=['GET', 'POST'])
def update_podcast(podcast_id):
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
    update_form = UpdateForm()
    picked_podcast = mongo.db.podcasts.find_one({'_id': ObjectId(podcast_id)})

  if request.method == 'GET':
    update_form.podcast_title.data = picked_podcast['podcast_title'] 
    update_form.podcast_imgurl.data = picked_podcast['podcast_imgurl'] 
    update_form.origin.data = picked_podcast['origin']
    update_form.release_year.data = picked_podcast['release_year'] 
    update_form.description.data = picked_podcast['description'] 
    update_form.is_favourite.data = picked_podcast['is_favourite'] 
    update_form.no_episodes.data = picked_podcast['no_episodes']
    update_form.podcast_link.data = picked_podcast['podcast_link']

  elif update_form.validate_on_submit():
    mongo.db.podcasts.update_one( {'_id': ObjectId(podcast_id)},
    {'$set': 
            {'podcast_title': update_form.podcast_title.data,
            'podcast_imgurl': update_form.podcast_imgurl.data,
            'origin': update_form.origin.data,
            'release_year': update_form.release_year.data,
            'description': update_form.description.data,
            'is_favourite': update_form.is_favourite.data,
            'no_episodes': update_form.no_episodes.data,
            'podcast_link': update_form.podcast_link.data}
            })
    flash(f'Podcast details updated sucessfully.', 'success')
    return redirect(url_for('your_account'))

  else:
    flash(f'Error updating podcast. Please try again', 'info')
    return redirect(url_for('your_account'))

  return render_template('podcast.html', form = update_form, podcast = picked_podcast)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)
