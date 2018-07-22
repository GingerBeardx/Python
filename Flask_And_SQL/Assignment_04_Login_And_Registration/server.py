from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from validate import validate_registration
import md5

app = Flask(__name__)
app.secret_key = "AMessageFromTheKing"
mysql = MySQLConnector(app, 'login')

# Landing page
@app.route('/')
def index():
    # checks session variables: user and button states
    if not 'show_register' in session:
        session['show_register'] = []
    if not 'show_login' in session:
        session['show_login'] = []
    if not 'show_logout' in session:
        session['show_logout'] = []
    if not 'user_name' in session:
        session['user_name'] = []
    
    # if no user is logged in, display register and login buttons
    if len(session['user_name']) < 2:
        session['show_register'] = 'inline-block'
        session['show_login'] = 'inline-block'
        session['show_logout'] = 'd-none'
    return render_template('index.html')

# When user clicks register button
@app.route('/register')
def register():
    #set button states
    session['show_register'] = 'd-none'
    session['show_login'] = 'inline-block'
    return render_template('register.html')

# Once user submits registration info
@app.route('/registration', methods=['POST'])
def registration():
    # Run form validation
    if validate_registration(request.form) == True:
        # If validation fails, then display errors on register page
        return redirect('/register')
    # If registration validation is passed, update database
    hased_password = md5.new(request.form['password']).hexdigest()
    query = "INSERT INTO users (email, password, first_name, last_name, created_at, updated_at) VALUES (:email, :password, :first_name, :last_name, NOW(), NOW());"
    data = {
        'email': request.form['email'],
        'password': hased_password,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
    }
    mysql.query_db(query, data)
    # Create flash message for successful registration and log user in.
    flash('Congratulations! User {} {} has been successfully registered!'.format(request.form['first_name'], request.form['last_name']), 'success')
    session['user_name'] = '{} {}'.format(request.form['first_name'], request.form['last_name'])
    flash('User: {} has been successfully logged in!'.format(session['user_name']), 'success')
    return redirect('/loggedin')

# When the user has successfully logged in
@app.route('/loggedin')
def loggedin():
    # Set button states: hide login and register and show logout
    session['show_login'] = "d-none"
    session['show_register'] = "d-none"
    session['show_logout'] = "inline-block"
    # Get user info from database so it can be displayed on the dash
    query = "SELECT email, password, first_name, last_name, DATE_FORMAT(created_at, '%m/%d/%Y %l:%i %p') AS time FROM users"
    users = mysql.query_db(query)
    return render_template('dash.html', all_users=users)

# Page for registered users to login
@app.route('/login')
def login():
    # Set button states
    session['show_login'] = 'd-none'
    session['show_register'] = 'inline-block'
    return render_template('login.html')

# Route for validating login info
@app.route('/logcheck', methods=['POST'])
def logcheck():
    # Check database for existing user
    query = "SELECT email, password, first_name, last_name FROM users WHERE email = :email"
    data = {
        'email': request.form['email']
    }
    user = mysql.query_db(query, data)
    # If user does not exist, display error
    if user == []:
        flash('User does not exist. Please confirm info or register.', 'danger')
        return redirect('/login')
    # If user exists, check password against what is stored in database
    hashed_password = md5.new(request.form['password']).hexdigest()
    # If password is incorrect, show error
    if user[0]['password'] != hashed_password:
        flash('Password for user is incorrect.', 'danger')
        return redirect('/login')
    # If password is correct, log user in
    session['user_name'] = '{} {}'.format(user[0]['first_name'], user[0]['last_name'])
    flash('User: {} has been successfully logged in!'.format(session['user_name']), 'success')
    return redirect('/loggedin')

# If user clicks logout button, clear the session and route back to landing page
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
