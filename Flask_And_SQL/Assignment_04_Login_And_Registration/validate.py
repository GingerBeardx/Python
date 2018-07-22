from flask import Flask, flash
from validate_email import validate_email

def validate_registration(email):
    errors = False
    #verify an e-mail address was entered
    if len(email) < 1:
        flash('Please enter your email address', 'danger')
        errors = True
        return errors
    
    # validate e-mail
    is_valid = validate_email(email)
    if is_valid == False:
        flash('Please enter a valid email address', 'danger')
        errors = True
        return errors
    
    return errors

