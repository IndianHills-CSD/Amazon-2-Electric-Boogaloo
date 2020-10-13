"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, session
from Amazon2 import app
app.secret_key = "abc"
from Amazon2 import dbHelper as db

@app.route('/')
@app.route('/login')
@app.route('/login/<int:status>')
def login():
    """Renders the home page."""
    message = ""
    status = request.args.get('status')
    if status != None:
        status = int(status)
        if status == 1:
            message = "Invalid Credentials"
        
    return render_template(
        'login.html',
        message = message
    )

@app.route('/home')
def home():
    """Renders the contact page."""
    if not session.get('logged_in'):
        return render_template(
            'login.html',
            message='Logged out due to inactivity.')

    return render_template(
        'home.html',
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/register')
def register():
    """Renders the register new user page."""
    return render_template(
        'register.html',
        title='Register'
    )

@app.route('/checkout')
def checkout():
    """Renders the register new user page."""
    return render_template(
        'checkout.html',
        title='Checkout'
    )


#Form Submission Methods

@app.route('/login_form',methods=['GET', 'POST'])
def check_login():
    session['logged_in'] = False
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        remember = request.form['remember']
        session['logged_in'] = db.dbHelper.login(username,password)
        

    
    if session['logged_in'] == True:
        session['username'] = username
        return  render_template(
            'home.html',
            title='Home',
            message= "Welcome "+ session['username'])
    else:
        return redirect(
            '/login?status=1')


@app.route('/register_form',methods=['GET', 'POST'])
def register_form():

    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        db.dbHelper.addNewUser(email,username,password)

    
    
    return render_template(
        'login.html',
        message='Log in with new credentials.')