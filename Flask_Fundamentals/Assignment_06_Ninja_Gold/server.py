from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.key = random.randrange(0,15678895)
app.secret_key = str(app.key)


def update_total_gold():
    try:
        session['total_gold'] += random.randrange(0,51)
    except KeyError:
        session['total_gold'] = 0

@app.route('/')
def index():
    print session
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def proc_money():
    update_total_gold()
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_gold():
    session['total_gold'] = 0
    return redirect('/')

app.run(debug=True)