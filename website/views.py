from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db 
import json
import jsonify

#Defining the name of the blueprint
views = Blueprint('views',__name__)

#name of the blueprint which is line 4
#Home page of the website
@views.route('/', methods = ['GET','POST'])
@login_required #need to login to get to home page
def home():

    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short',category="error")
        else:
            new_note = Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!",category='success')


    return render_template("home.html", user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    #what comes from the JS
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
