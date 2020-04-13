from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), 
                                                                    EqualTo('password', 
                                                                    message='Passwords must match.')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()]) 
    submit = SubmitField('Login')

class AddForm(FlaskForm):
    podcast_title = StringField('Title: ', validators=[DataRequired()])
    podcast_imgurl = StringField('Podcast image: ', validators=[DataRequired()])
    origin = RadioField('Origin: ', choices=[
                                    (1,'UK'), (2,'Australia'), (3,'USA')],
                                    default=1, coerce=int, validators=[DataRequired()])
    release_year = StringField('Release year: ', validators=[DataRequired()])
    description = TextAreaField('Description: ', validators=[DataRequired(), Length(max=500)])
    is_favourite = BooleanField('Favourite: ')
    no_episodes = StringField('Number of episodes: ', validators=[DataRequired()])
    podcast_link = StringField('Link to podcast website: ', validators=[DataRequired()])
    submit = SubmitField('Add podcast')

class UpdateForm(FlaskForm):
    podcast_title = StringField('Title: ', validators=[DataRequired()])
    podcast_imgurl = StringField('Podcast image: ', validators=[DataRequired()])
    origin = RadioField('Origin: ', choices=[
                                    (1,'UK'), (2,'Australia'), (3,'USA')],
                                    default=1, coerce=int, validators=[DataRequired()])
    release_year = StringField('Release year: ', validators=[DataRequired()])
    description = TextAreaField('Description: ', validators=[DataRequired(), Length(max=500)])
    is_favourite = BooleanField('Favourite: ')
    no_episodes = StringField('Number of episodes: ', validators=[DataRequired()])
    podcast_link = StringField('Link to podcast website: ', validators=[DataRequired()])
    submit = SubmitField('Save changes')