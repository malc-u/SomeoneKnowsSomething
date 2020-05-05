import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, AddForm, UpdateForm, DeleteForm, ChangePasswordForm
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
def index():
  """
  Function that opens home/index page of the project.
  """  
  return render_template('pages/index.html',
                          title="True crime podcasts",
                           head="True crime podcasts")


@app.route('/login', methods=['GET', 'POST'])
def login():
  """
  Function allowing to login into the page using Login Form.
  It check whether username provided matches the one stored in users collection of 
  a database.
  It also checks whether hashed form of a password provided in the form is a match too.
  Check_password_hash part is based on example no 9 from this page
  https://www.programcreek.com/python/example/58659/werkzeug.security.check_password_hash
  but it was amended and updated to suit the needs of this app
  """
  form_login = LoginForm()

  if form_login.validate_on_submit():
    existing_user = mongo.db.users.find_one({'username': form_login.username.data})
    
    if not existing_user:
      flash(f'Username not found. Please try again or register.', 'danger')
      return redirect(url_for('register'))

    elif existing_user is not None and check_password_hash(existing_user['password'], form_login.password.data):
      session['username'] = request.form.get('username')
      return redirect(url_for('my_account'))
    
    flash(f'Password incorrect. Please try again.', 'danger')
    return redirect(url_for('login'))

  return render_template('pages/login.html', 
                          title = 'Login', 
                          form = form_login,
                          head="Please Login") 

@app.route('/register', methods=['GET', 'POST'])
def register():
  """
  Function that allows to register new user by creating saving into database(users 
  collection) new username and new password (both provided in a registration form). 
  Password to be stored in a hashed form.
  """ 
  form_register = RegistrationForm()

  if form_register.validate_on_submit():
    existing_username = mongo.db.users.find_one({'username': request.form['username']})
 
    if not existing_username:
      entered_password = request.form['password']
      password_hashed = generate_password_hash(entered_password)
      mongo.db.users.insert({'username': form_register.username.data,
                                    'password': password_hashed})
      session['username'] = request.form.get('username')
      flash(f'Your account has been created.', 'success')
      return redirect(url_for('index'))
      
    else:
      flash(f'Username already taken. Please try another one.', 'danger')
      return redirect(url_for('register'))

  return render_template('pages/register.html', 
                          title='Register',
                          form=form_register,
                          head='Register to Listen Now')

@app.route('/logut')
def logout():
  """
  Function that logs the user out and clears the session cookie.
  """ 
  session.clear()
  return redirect(url_for('index'))

@app.route('/recommended')
def recommended():
  """
  Function that opens recommended page by searchnign podcasts collection of a database
  for all content with value of a key "is_recommended" set to "True"
  """ 
  return render_template('pages/recommended.html', 
                          podcasts = mongo.db.podcasts.find({"is_recommended": True}), 
                          head = "Recommended",
                          title='Recommended')

@app.route('/favourites')
def favourites():
  """
  Function that opens recommended page by searchning podcasts collection of a database
  for content with value of a key "is_favourite" set to "True" and 
  then limits output to 8 results only.
  """ 
  return render_template('pages/recommended.html', 
                          podcasts = mongo.db.podcasts.find({"is_favourite": True}).limit(8), 
                          head = "Users favourites",
                          title='Users favourites')

@app.route('/british')
def british():
  """
  Function that checks whether user is logged in. For logged in user it opens 
  an origin page by searchning podcasts collection of a database
  for content with value of an key "origin" set to "1" and presents it to a user as
  of a British origin.
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
    return redirect(url_for('login'))
  else:
    return render_template('pages/origin.html', 
                            podcasts = mongo.db.podcasts.find({"origin": 1}),
                            origin = 'United Kingdom',
                            title='British podcasts')

@app.route('/australian')
def australian():
  """
  Function that checks whether user is logged in. For logged in user it opens 
  an origin page by searchning podcasts collection of a database
  for content with value of an key "origin" set to "2" and presents it to a user as 
  of an Australian origin.
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
    return redirect(url_for('login'))
  else:
    return render_template('pages/origin.html', 
                            podcasts = mongo.db.podcasts.find({"origin": 2}),
                            origin = 'Australia',
                            title='Australian podcasts')

@app.route('/american')
def american():
  """
  Function that checks whether user is logged in. For logged in user it opens 
  an origin page by searchning podcasts collection of a database
  for content with value of an key "origin" set to "3" and presents it to a user as 
  of an American origin.
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
    return redirect(url_for('login'))
  else:
    return render_template('pages/origin.html', 
                            podcasts = mongo.db.podcasts.find({"origin": 3}),
                            origin = 'USA',
                            title='American podcasts')

@app.route('/read_more/<podcast_id>', methods=['GET', 'POST'])
def read_more(podcast_id):
  """
  Function that dispalys read more page with details of clicked by the user podcast.
  It searched database collection podcasts for the podcast using a value "ObjectId"
  of the key "_id"
  """ 
  picked_podcast = mongo.db.podcasts.find_one({'_id': ObjectId(podcast_id)})

  return render_template('pages/more.html', 
                          podcast = picked_podcast,
                          title='Read more about podcast')

@app.route('/my-account')
def my_account():
  """
  Function that checks whether user is logged in. For logged in user it opens 
  account dashboard and displays podcasts of this user by searchning podcasts collection 
  of a database for content with value of an key "username" set to "username" 
  from session.
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
    return redirect(url_for('login'))
  else:
    current_user = session['username']
    return render_template('pages/account.html', 
                            podcasts = mongo.db.podcasts.find({"username": current_user}), 
                            head="Account Dashboard", 
                            title="Account dashboard")
    

@app.route('/podcast/add', methods=['GET', 'POST'])
def podcast_add():
  """
  Function that checks whether user is logged in. For logged in user it opens 
  page with a form that allows user to add new content to the database.
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
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
        flash(f'Your podcast has been added', 'success')
        return redirect(url_for('my_account'))

  return render_template('pages/podcast-add.html', 
                          form=add_form,
                          title='Add new podcast',
                          head='Add Podcast')
    
@app.route('/podcast/update/<podcast_id>', methods=['GET', 'POST'])
def podcast_update(podcast_id):
  """
  Function that checks whether user is logged in. For logged in user it opens 
  page with a form that allows user to edit existing content to the database.
  It searches collection podcasts in the detabase and displays pre-filled in form
  with the content of a podcast found using value "ObjectId(podcast_id)" of a key "_id".
  Used request.method == 'GET' following advice from 
  https://romain.dorgueil.net/wiki/python/wtforms and https://stackoverflow.com/a/23714791
  to populate update form with existing in database details for the podcast that user 
  wants to amend.  
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
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
    return redirect(url_for('my_account'))

  else:
    flash(f'Error updating podcast. Please try again', 'danger')
    return redirect(url_for('my_account'))

  return render_template('pages/podcast-update.html', 
                          form = update_form, 
                          podcast = picked_podcast,
                          title='Update podcast details',
                          head='Edit Podcast')

@app.route('/podcast/delete/<podcast_id>', methods=['GET', 'POST'])
def podcast_delete(podcast_id):
  """
  Function that checks whether user is logged in. For logged in user it opens page with
  more details of podcast to be deleted and short form to be submitted for a podcast 
  to be deleted. It searched database collection podcasts for the podcast using a 
  value "ObjectId(podcast_id)" of the key "_id".
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'danger')
    return redirect(url_for('login'))
  else:
    delete_form = DeleteForm()
    picked_podcast = mongo.db.podcasts.find_one({'_id': ObjectId(podcast_id)})

  if delete_form.validate_on_submit():
    existing_username = session['username']
    existing_user = mongo.db.users.find_one({'username': existing_username})
    if existing_user and check_password_hash(existing_user['password'], delete_form.password.data):
      mongo.db.podcasts.delete_one( {'_id': ObjectId(podcast_id)})
      flash(f'Podcast deleted', 'success')
      return redirect(url_for('my_account'))
    else:
        flash(f'Oops, something went wrong. Please try again', 'danger')

  return render_template('pages/podcast-delete.html', 
                          form = delete_form , 
                          podcast = picked_podcast,
                          title='Delete podcast')

@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
  """
  Function that checks whether user is logged in. For logged in user it opens page with
  a form that allows user to change their password.
  It searches database collection users for a value of a key "username" that is 
  identical to "username" in session. It then replaces existing in the database password
  with a hashed form of the one from the form.
  For users that are not logged in it redirects to login page.
  """ 
  if 'username' not in session:
    flash(f'Oops... you need to be logged in to see this page.', 'info')
    return redirect(url_for('login'))
  else:
    change_form = ChangePasswordForm()
    current_user = session['username']

  if request.method == 'GET':
    change_form.new_password.data 
    change_form.confirm_password.data 

  elif change_form.validate_on_submit():
    entered_password = request.form['new_password']
    password_hashed = generate_password_hash(entered_password)
    mongo.db.users.update_one( {'username': current_user},
    {'$set': 
            {'password': password_hashed}
            })
    flash(f'Password updated sucessfully.', 'success')
    return redirect(url_for('my_account'))

  else:
    flash(f'Error updating password. Please try again', 'danger')
    return redirect(url_for('my_account'))

  return render_template('pages/settings.html', 
                          form = change_form,
                          head='Password change',
                          title='Change password')

# Error Handling of 404 & 500
@app.errorhandler(404)
def page_not_found(e):
    '''
    Error handler as supplied by Flask 
    https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/- 
    '''
    return render_template('pages/404.html', 
                            title="'404' Page Not Found",
                            head='404 - Page Not Found'), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=False)
