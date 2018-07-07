from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'xv02A56!#%$'

def generate_num():
    app.secret_number = random.randrange(1,101)

@app.route('/')
def index():
    generate_num()
    session['number'] = app.secret_number
    return render_template('index.html', session=session)

@app.route('/guess', methods=['POST'])
def guess():
    u_guess = int(request.form['guess'])
    if u_guess > session['number']:
        return render_template('_too-high.html')
    elif u_guess < session['number']:
        return render_template('_too-low.html')
    else:
        return render_template('_correct.html')

@app.route('/reset', methods=['POST'])
def reset():
    generate_num()
    return redirect('/')


app.run(debug=True)
