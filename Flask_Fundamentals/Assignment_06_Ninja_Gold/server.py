from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.key = random.randrange(0,15678895)
app.secret_key = str(app.key)


def update_total_gold(add_gold):
    try:
        session['total_gold'] += add_gold
    except KeyError:
        session['total_gold'] = 0

@app.route('/')
def index():
    update_total_gold(0)
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def proc_money():
    if request.form['building'] == 'farm':
        add_gold = random.randrange(10, 21)
    elif request.form['building'] == 'cave':
        add_gold = random.randrange(5, 11)
    elif request.form['building'] == 'house':
        add_gold = random.randrange(2, 6)
    elif request.form['building'] == 'casino':
        add_gold = random.randrange(-50, 51)
    update_total_gold(add_gold)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset_gold():
    session['total_gold'] = 0
    return redirect('/')

app.run(debug=True)