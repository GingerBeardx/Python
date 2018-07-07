from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0

def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sumSessionCounter()
    return render_template('index.html')

@app.route('/add_two', methods=["POST"])
def add_two():
    sumSessionCounter()
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)