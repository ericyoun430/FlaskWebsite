from flask import Blueprint, render_template

#Defining the name of the blueprint
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    #text is now a variable you can pass to the template
    return render_template('login.html', boolean=True)

@auth.route('/sign-up')
def logout():
    return render_template('sign_up.html')

@auth.route('/logout')
def signout():
    return "<p>Logout<p>"
