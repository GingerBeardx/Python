from flask import Flask, flash
from validate_email import validate_email

def validate_registration(form):
    errors = False

    # name validation
    if len(form['first_name']) < 2 or len(form['last_name']) < 2:
        flash('Names must be at least 2 characters long', 'danger')
        errors = True

    # validate e-mail
    if len(form['email']) < 1:
        flash('Please enter your email address', 'danger')
        errors = True
    
    is_valid = validate_email(form['email'])
    if is_valid == False:
        flash('Please enter a valid email address', 'danger')
        errors = True

    # password checks
    password = form['password']
    if len(password) < 8:
        flash('Password should be at least 8 digits long', 'danger')
        errors = True
    if password.isalpha() or password.isdigit():
        flash('Password should contain at least one number [0-9] and at least one alpha character [a-z]', 'danger')
        errors = True
    if password.islower():
        flash('Password should contain at least one capitalized alpha character', 'danger')
        errors = True
    if password != form['password_confirm']:
        flash('Passwords do not match', 'danger')
        errors = True
    
    return errors

def validate_login(form):
    errors = False
    # validate e-mail
    if len(form['email']) < 1:
        flash('Please enter your email address', 'danger')
        errors = True    
    is_valid = validate_email(form['email'])
    if is_valid == False:
        flash('Please enter a valid email address', 'danger')
        errors = True
    # password checks
    password = form['password']
    if len(password) < 8:
        flash('Password should be at least 8 digits long', 'danger')
        errors = True
    return errors