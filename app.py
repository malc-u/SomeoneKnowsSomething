import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo
from os import path


if path.exists("env.py"):
  import env
  
app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.getenv("MONGO_DBNAME")
app.config['MONGO_URI'] = os.getenv("MONGODB_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/recommended')
def recommended():
  return render_template('recommended.html', 
  podcasts = mongo.db.podcasts.find({"is_recommended": True}))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)
