from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(), 
                                                                    EqualTo('password', 
                                                                    message='Passwords must match.')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()]) 
    submit = SubmitField('Login')

class AddForm(FlaskForm):
    podcast_title = StringField('Title:', validators=[DataRequired()])
    podcast_imgurl = StringField('Podcast Image Link:', validators=[DataRequired()])
    origin = RadioField('Origin:', choices=[
                                    (1,'UK'), (2,'Australia'), (3,'USA')],
                                    default=1, coerce=int, validators=[DataRequired()])
    release_year = StringField('Release Year:', validators=[DataRequired(), Length(min=4, max=4)])
    description = TextAreaField('Description:', validators=[DataRequired(), Length(max=500)])
    is_favourite = BooleanField('Favourite:')
    no_episodes = StringField('Number Of Episodes:', validators=[DataRequired()])
    podcast_link = StringField('Link To Podcast Website:', validators=[DataRequired()])
    submit = SubmitField('Add Podcast')

class UpdateForm(FlaskForm):
    podcast_title = StringField('Title: ', validators=[DataRequired()])
    podcast_imgurl = StringField('Podcast Image Link:', validators=[DataRequired()])
    origin = RadioField('Origin:', choices=[
                                    (1,'UK'), (2,'Australia'), (3,'USA')],
                                    default=1, coerce=int, validators=[DataRequired()])
    release_year = StringField('Release Year:', validators=[DataRequired(), Length(min=4, max=4)])
    description = TextAreaField('Description:', validators=[DataRequired(), Length(max=500)])
    is_favourite = BooleanField('Favourite:')
    no_episodes = StringField('Number Of Episodes:', validators=[DataRequired()])
    podcast_link = StringField('Link To Podcast Website:', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

class DeleteForm(FlaskForm):
    password = PasswordField('Enter Password To Delete:', validators=[DataRequired()])
    submit = SubmitField('Delete')

class ChangePasswordForm(FlaskForm):
    new_password = PasswordField('Enter New Password:', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password:', validators=[DataRequired(), 
                                                                    EqualTo('new_password', 
                                                                    message='Passwords must match.')])
    submit = SubmitField('Change now')