from flask import Flask, render_template, session, redirect, request, flash
app = Flask(__name__)
app.secret_key = 'keepitsecretkeepitsafe'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash('Name cannot be emppty!')
    else:
        flash('Success! Your name is {}'.format(request.form['name']))
    return redirect('/')
app.run(debug=True)