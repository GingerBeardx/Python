from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from validate import validate_registration

app = Flask(__name__)
app.secret_key = "AMessageFromTheKing"
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    if not 'show_button' in session:
        session['show_button'] = []
    if not 'user_name' in session:
        session['user_name'] = []
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
    flash('Congratulations! User {} has been successfully registered'.format(request.form['first_name']), 'success')
    session['user_name'] = request.form['first_name']
    return redirect('/loggedin')

@app.route('/loggedin')
def loggedin():
    flash('User: {} has been successfully logged in!'.format(session['user_name']), 'success')
    return render_template('dash.html')

app.run(debug=True)
