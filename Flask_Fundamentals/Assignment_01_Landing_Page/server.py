from flask import Flask, render_template
app = Flask(__name__)

#define the root route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas/')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new/')
def dojos_new():
    return render_template('new-ninja.html')
    
app.run(debug=True)