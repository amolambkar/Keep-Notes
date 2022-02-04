from crypt import methods
from flask import Blueprint, redirect, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/update-note/<int:id>',methods=['POST'])
def update_note(id):
    if request.method == 'POST':
        note = request.form['note-data']

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            keeped_note = Note.query.filter_by(id=id).first()
            keeped_note.data = note
            db.session.add(keeped_note)
            db.session.commit()
            # flash('Note updated!', category='success')
            return redirect("/")
        return render_template("home.html", user=current_user)

@views.route('/demo', methods=['GET'])
def demo():
    return render_template("demo.html",user=current_user)