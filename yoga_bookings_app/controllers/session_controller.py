import imp
from flask import Blueprint, Flask, redirect, render_template, request
from models.session import Session
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.session_repository as session_repository


session_blueprint = Blueprint("session", __name__)

#INDEX
@session_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    sessions = sorted(sessions, key=lambda d: d.date)
    return render_template("sessions/index.html", sessions=sessions)


# SHOW
@session_blueprint.route("/sessions/<id>")
def show_session(id):
    session = session_repository.select(id)
    bookings = booking_repository.select_all_bookings_by_session_id(id)
    return render_template("sessions/show.html", session = session, bookings = bookings)


#NEW
@session_blueprint.route("/sessions/new")
def new_session():
    return render_template("sessions/new.html")


#CREATE
@session_blueprint.route("/sessions", methods = ["POST"])
def create_session():
    yoga_type = request.form["yoga_type"]
    duration = request.form["duration"]
    date = request.form["date"]
    time = request.form["time"]
    new_session = Session(yoga_type, duration, date, time)
    
    success = session_repository.save(new_session)
    if success:
        return redirect("/sessions/new/success")
    return redirect("/sessions/new/oops")

#CREATE OOPS
@session_blueprint.route("/sessions/new/oops", methods = ["GET"])
def create_session_fail():
    return render_template("sessions/new_oops.html")

#CREATE HOORAY
@session_blueprint.route("/sessions/new/success", methods = ["GET"])
def create_session_success():
    return render_template("sessions/new_success.html")



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
    date = request.form["date"]
    time = request.form["time"]

    session = Session(yoga_type, duration, date, time, id)

    session_repository.update(session)
    session = session_repository.select(id)
    bookings = booking_repository.select_all_bookings_by_session_id(id)
    # print(type(updated_session.date))
    # print("what3 " + session2.date + " time " +session2.time+ ": "+session2.duration + ":" + session2.yoga_type)
    return render_template("/sessions/show.html", session = session, bookings = bookings)

    



#DELETE
@session_blueprint.route("/sessions/<id>/delete", methods = ["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")