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
    session['show_button'] = 'inline-block'
    return render_template('index.html')

@app.route('/register')
def register():
    session['show_button'] = 'd-none'
    return render_template('register.html')
    
app.run(debug=True)
