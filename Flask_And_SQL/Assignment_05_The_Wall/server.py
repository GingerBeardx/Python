from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
from validate import validate_registration
import md5

app = Flask(__name__)
app.secret_key = "AWallCouldntKeepTheHunsFromInvading"
mysql = MySQLConnector(app, 'thewall')

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
    if not 'user_id' in session:
        session['user_id'] = []
    
    # if no user is logged in, display register and login buttons
    if len(session['user_name']) < 2:
        session['show_register'] = 'inline-block'
        session['show_login'] = 'inline-block'
        session['show_logout'] = 'd-none'
    return render_template('index.html')

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
    return redirect('/thewall')

# When the user has successfully logged in
@app.route('/thewall')
def thewall():
    # Set button states: hide login and register and show logout
    session['show_login'] = "d-none"
    session['show_register'] = "d-none"
    session['show_logout'] = "inline-block"
    # Get user messages from database so it can be displayed on the dash
    query = "SELECT CONCAT(users.first_name, ' ', users.last_name) AS user_name, DATE_FORMAT(messages.updated_at, '%M %D %Y') AS message_date, messages.message, messages.message_id FROM users JOIN messages ON users.user_id = messages.user_id ORDER BY messages.updated_at DESC"
    messages = mysql.query_db(query)
    # Get comments from database
    query = "SELECT comments.message_id, comments.comment, DATE_FORMAT(comments.updated_at, '%M %D %Y') AS comment_date, CONCAT(users.first_name, ' ', users.last_name) AS commenter FROM comments LEFT JOIN messages ON comments.message_id = messages.message_id LEFT JOIN users ON comments.user_id = users.user_id ORDER BY comments.updated_at ASC"
    comments = mysql.query_db(query)
    return render_template('wall.html', all_messages=messages, all_comments=comments)

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
    query = "SELECT user_id, email, password, first_name, last_name FROM users WHERE email = :email"
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
    session['user_id'] = user[0]['user_id']
    flash('User: {} has been successfully logged in!'.format(session['user_name']), 'success')
    return redirect('/thewall')

# If user clicks logout button, clear the session and route back to landing page
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/addmessage', methods=['POST'])
def add_message():
    # Check for a valid length for a message
    print "*" * 80
    print type(request.form['message'])
    if len(request.form['message']) < 5:
        flash('Messages should be longer than 5 characters', 'warning')
        return redirect('/thewall')
    # If validated insert message into database
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW());"
    data = {
        'user_id': session['user_id'],
        'message': request.form['message']
    }
    mysql.query_db(query, data)
    flash('New message posted to The Wall', 'info')
    return redirect('/thewall')

app.run(debug=True)