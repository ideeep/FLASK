# create a new flask based application
from flask import Flask

# create flask app
app = Flask(__name__) #entry point for Flask

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return 'Welcome!'
if __name__ == '__main__':
    app.run()