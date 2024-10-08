#!/usr/bin/env python3
"""
Forms for user authentication and interaction in the flask_ambrosial module.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.validators import ValidationError
from flask_login import current_user
from flask_ambrosial.models import User

class RegistrationForm(FlaskForm):
    """
    Form for user registration.
    """
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """
        Validate that the username is not already taken.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one.'
            )

    def validate_email(self, email):
        """
        Validate that the email is not already taken.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.'
            )

class LoginForm(FlaskForm):
    """
    Form for user login.
    """
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    """
    Form for updating user account information.
    """
    username = StringField(
        'Username', validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    picture = FileField(
        'Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])]
    )
    submit = SubmitField('Update')

    def validate_username(self, username):
        """
        Validate that the new username is not already taken.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'That username is taken. Please choose a different one.'
                )

    def validate_email(self, email):
        """
        Validate that the new email is not already taken.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'That email is taken. Please choose a different one.'
                )

class RequestResetForm(FlaskForm):
    """
    Form for requesting a password reset.
    """
    email = StringField(
        'Email', validators=[DataRequired(), Email()]
    )
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        """
        Validate that the email exists in the database.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                'There is no account with that email. You must register first.'
            )

class ResetPasswordForm(FlaskForm):
    """
    Form for resetting the password.
    """
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Reset Password')

class CommentForm(FlaskForm):
    """
    Form for posting a comment.
    """
    content = TextAreaField(
        'Content', validators=[DataRequired()]
    )
    submit = SubmitField('Post Comment')

class ReplyForm(FlaskForm):
    """
    Form for posting a reply to a comment.
    """
    content = TextAreaField(
        'Content', validators=[DataRequired()]
    )
    submit = SubmitField('Post Reply')
