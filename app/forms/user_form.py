from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from app.models.user import User


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember')
    submit = SubmitField('login')


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('repeat', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self, username):
        invalid = ['mimin', 'merbot', 'admin', 'momod', 'ngalim', 'nsiregar', 'wanperfeksyot', 'wakdoyok']
        if username.data in invalid:
            raise ValidationError('username already registered')
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('username already registered')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('email already registered')