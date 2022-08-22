from flask import Blueprint, Flask, redirect, render_template, request
from models.session import Session
import repositories.session_repository as session_repository

session_blueprint = Blueprint("session", __name__)

#INDEX
@session_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)


#NEW
@session_blueprint.route("/sessions/new")
def new_session():
    return render_template("sessions/new.html")


#CREATE
@session_blueprint.route("/sessions", methods = ["POST"])
def create_session():
    yoga_type = request.form["yoga_type"]
    duration = request.form["duration"]
    new_session = Session(yoga_type, duration)
    session_repository.save(new_session)
    return redirect("/sessions")


#EDIT
@session_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template("sessions/edit.html", session = session)


#UPDATE
@session_blueprint.route("/sessions/<id>", methods = ["POST"])
def update_session(id):
    yoga_type = request.form["yoga_type"]
    duration = request.form["duration"]
    session = Session(yoga_type, duration, id)
    session_repository.update(session)


#DELETE
@session_blueprint.route("/sessions/<id>/delete", methods = ["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")