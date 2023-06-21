from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #from init.py file
from flask_login import login_user, login_required, logout_user, current_user
#Defining the name of the blueprint
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        #filter the db so we get the first value with that email
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully', category="success")
                #Don't have to login again all the time
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category="error")
        else:
            flash('Email does not exist', category="error")


    #text is now a variable you can pass to the template
    return render_template('login.html', user=current_user)

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists',category="error")
        #The categories are created by yourself
        elif len(email) < 4:
            flash('Email must be greater than 3 characters',category="error")
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters',category="error")
        elif password1 != password2:
            flash('Passwords don\'t match',category="error")
        elif len(password1) < 7:
            flash('Password must be at least 7 characters',category="error")
        else:
            new_user = User(email=email,firstName=firstName,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Accounted created!',category="success")

            #views is the name of the blueprint and home is the name of the function
            return redirect(url_for('views.home'))
             


    return render_template('sign_up.html',user=current_user)

@auth.route('/logout')
@login_required #need to login until you logout
def signout():
    logout_user()
    return redirect(url_for('auth.login'))
