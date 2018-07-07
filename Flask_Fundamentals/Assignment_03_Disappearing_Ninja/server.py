from flask import Flask, render_template, url_for
app = Flask(__name__)
valid_cols = ['red', 'blue', 'purple', 'orange']

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ninja/')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def nin_color(color):
    if color in valid_cols: 
        return render_template(color + ".html")
    else:
        return render_template('error.html')
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

app.run(debug=True)