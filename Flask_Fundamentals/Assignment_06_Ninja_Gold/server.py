from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'xv02A56!#%$'

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)