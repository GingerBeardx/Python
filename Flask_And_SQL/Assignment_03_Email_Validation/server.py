from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from validate_email import validate_email

app = Flask(__name__)
app.secret_key = "WeHaveTheMeats"
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/address', methods=['POST'])
def address():
    #validate e-mail
    print request.form['email']
    errors = False

    #verify an e-mail address was entered
    if len(request.form['email']) < 1:
        flash('Please enter your email address', 'danger')
        errors = True
    
    # validate e-mail
    is_valid = validate_email(request.form['email'])
    if is_valid == False:
        flash('Please enter a valid email address', 'danger')
        errors = True
    
    # if validation did not pass
    if errors == True:
        return redirect('/')
    
    # if validation passes

    # update the database with new address
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW());"
    data = {
        'email': request.form['email'],
    }
    mysql.query_db(query, data)

    # create flash message
    email = request.form['email']
    flash('The email address you entered ({}) is a VALID email address! Thank you!'.format(email), 'success')
    return redirect('/success')

@app.route('/success')
def addresses():
    query = 'SELECT email, created_at FROM emails'
    users = mysql.query_db(query)
    return render_template('addresses.html', email_data=users)

app.run(debug=True)
