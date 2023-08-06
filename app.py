'''
The main application file for server
'''

import database
import user

from flask import Flask, render_template, request, session, make_response, url_for, redirect


app = Flask(__name__, static_url_path='/static')  # '__main__'
app.secret_key = "Nuggets"


@app.route('/')
def home_template():
    return render_template('home.html')


        
@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else: # update to where we say user is not valid try again
        session['email'] = None

    return render_template("profile.html", email=session['email'])


@app.route('/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)
    
    return render_template('profile.html', email=session['email'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
