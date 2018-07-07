from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/sub', methods=['POST'])
def sub_form():
    return render_template('complete.html', form_data = request.form)


app.run(debug=True)