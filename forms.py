from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, URL
from wtforms import ValidationError
from flask_ckeditor import CKEditor, CKEditorField


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if username.data == 'admin':
            raise ValidationError('Username cannot be "admin". Please choose a different one.')

    def validate_email(self, email):
        if email.data == 'admin@example.com':
            raise ValidationError('Email cannot be "admin@example.com". Please choose a different one.')