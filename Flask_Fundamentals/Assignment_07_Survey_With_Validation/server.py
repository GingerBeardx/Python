from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
app.secret_key = "HubbaBubba"

@app.route('/')
def survey():
    return render_template('survey.html')

@app.route('/sub', methods=['POST'])
def sub_form():
    if len(request.form['your_name']) < 1:
        flash("Name cannot be blank")
        return render_template('survey.html')
    elif len(request.form['comment']) > 150:
        flash("Comment should not exceed 150 characters")
        return render_template('survey.html')
    return render_template('complete.html', form_data = request.form)


app.run(debug=True)