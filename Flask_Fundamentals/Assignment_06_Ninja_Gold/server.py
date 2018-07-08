from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.key = random.randrange(0,15678895)
app.secret_key = str(app.key)
app.count = 0

def init_vals():
    try:
        print session['total_gold']
        print session['strings']
    except KeyError:
        session['total_gold'] = 0
        session['strings'] ={}    

def update_strings(location, add_gold):
    string = "earned {} gold from {}".format(add_gold, location)
    session['strings'][app.count] = string
    app.count += 1
        

def gold_update(location):
    if location == 'farm':
        add_gold = random.randrange(10, 21)
    elif location == 'cave':
        add_gold = random.randrange(5, 11)
    elif location == 'house':
        add_gold = random.randrange(2, 6)
    elif location == 'casino':
        add_gold = random.randrange(-50, 51)
    update_strings(location, add_gold)
    session['total_gold'] += add_gold

@app.route('/')
def index():
    init_vals()
    return render_template('index.html', acts=session['strings'])

@app.route('/process_money', methods=['POST'])
def proc_money():
    gold_update(request.form['building'])
    app.count += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_gold():
    session['total_gold'] = 0
    session['strings'] = {}
    app.count = 0
    return redirect('/')

app.run(debug=True)