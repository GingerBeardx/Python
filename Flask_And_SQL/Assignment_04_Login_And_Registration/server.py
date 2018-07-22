from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from validate import validate_registration

app = Flask(__name__)
app.secret_key = "AMessageFromTheKing"
mysql = MySQLConnector(app, 'login')

@app.route('/')
def index():
    if not 'show_button' in session:
        session['show_button'] = []
    if not 'user_name' in session:
        session['user_name'] = []
    print "*" * 80
    print session
    session['show_button'] = 'inline-block'
    return render_template('index.html')

@app.route('/register')
def register():
    session['show_button'] = 'd-none'
    return render_template('register.html')

@app.route('/registration', methods=['POST'])
def registration():
    if validate_registration(request.form) == True:
        return redirect('/register')
    #Update database
    query = "INSERT INTO users (email, password, first_name, last_name, created_at, updated_at) VALUES (:email, :password, :first_name, :last_name, NOW(), NOW());"
    data = {
        'email': request.form['email'],
        'password': request.form['password'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
    }
    mysql.query_db(query, data)
    flash('Congratulations! User {} {} has been successfully registered'.format(request.form['first_name'], request.form['last_name']), 'success')
    session['user_name'] = '{} {}'.format(request.form['first_name'], request.form['last_name'])
    return redirect('/loggedin')

@app.route('/loggedin')
def loggedin():
    flash('User: {} has been successfully logged in!'.format(session['user_name']), 'success')
    query = "SELECT email, password, first_name, last_name, DATE_FORMAT(created_at, '%m/%d/%Y %l:%i %p') AS time FROM users"
    users = mysql.query_db(query)
    return render_template('dash.html', all_users=users)

@app.route('/login')
def login():
    return render_template('login.html')

app.run(debug=True)
