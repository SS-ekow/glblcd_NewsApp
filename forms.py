from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=40)])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=40)])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  
    submit = SubmitField('Sign Up')