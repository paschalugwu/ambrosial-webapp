#!/usr/bin/env python3

import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flask_ambrosial import mail

def save_picture(form_picture):
    """Save and resize the user's profile picture.

    Args:
        form_picture (FileStorage): The file containing the user's profile picture.

    Returns:
        str: The filename of the saved picture.
    """
    # Generate a random filename to avoid conflicts
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    # Resize the image and save it
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn


def send_reset_email(user):
    """Send a password reset email to the user.

    Args:
        user (User): The user object for whom the password reset email is sent.
    """
    # Generate a token for password reset
    token = user.get_reset_token()
    
    # Create and send the email message
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:

{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
