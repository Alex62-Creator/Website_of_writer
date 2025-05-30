from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

#Создаём класс EmailForm, который будет создавать форму для отправки письма на email
class EmailForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired("Required"), Email("email not correct")])
    text = TextAreaField('Message')
    submit = SubmitField('Send Message')