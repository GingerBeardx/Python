from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from validate import val_email

app = Flask(__name__)
app.secret_key = "WeHaveTheMeats"
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/address', methods=['POST'])
def address():
    #validate e-mail
    errors = val_email(request.form['email'])
    
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
    query = "SELECT id, email, DATE_FORMAT(created_at, '%m/%d/%Y %l:%i %p') AS time FROM emails"
    users = mysql.query_db(query)
    return render_template('addresses.html', email_data=users)

@app.route('/delete/<email_id>', methods=['POST'])
def delete(email_id):
    flash('The email address, {}, has been deleted.'.format(request.form['email']), 'danger')

    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)
