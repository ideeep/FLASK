# create a new flask based application
from flask import Flask, render_template, url_for, redirect

# create flask app
app = Flask(__name__) #entry point for Flask

@app.route('/')
def home():
    return "Hello World"

@app.route('/welcome')
def welcome():
    return 'Welcome!'

@app.route('/index')
def index():
    return render_template('index.html')
    #return redirect(url_for('index.html'))
if __name__ == '__main__':
    app.run()