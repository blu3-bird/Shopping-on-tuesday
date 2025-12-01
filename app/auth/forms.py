"""
Forms used for admin authentication within the application.

This module defines the login form required for admin access. It includes
validation for username, password, and an optional "remember me" flag.
These forms ensure secure and consistent authentication handling for admin users.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class adminForm(FlaskForm):
    """
    Form used for authenticating an admin user.

    This form validates the admin's login credentials, including username
    and password, and optionally supports a "remember me" login session.

    Fields:
        username (StringField): Admin username. Required; must be 3–40 characters.
        password (PasswordField): Admin password. Required.
        remember_me (BooleanField): Optional flag to remember the user’s session.
        submit (SubmitField): Button to submit the login form.

    Returns:
        adminForm: A validated form instance used for admin authentication.
    """

    username = StringField('Username',validators=[DataRequired(message='Username is required!'),Length(min=3, max=40, message='Username must be between 3 and 40.')])

    password = PasswordField('Password',validators=[DataRequired(message='Password is required!')])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')