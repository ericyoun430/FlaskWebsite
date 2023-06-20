from flask import Blueprint, render_template

#Defining the name of the blueprint
views = Blueprint('views',__name__)

#name of the blueprint which is line 4
#Home page of the website
@views.route('/')
def home():
    return render_template("home.html")
