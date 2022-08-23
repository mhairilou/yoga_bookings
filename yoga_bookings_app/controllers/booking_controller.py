from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking
from models.session import Session
from models.student import Student
import repositories.session_repository as session_repository
import repositories.student_repository as student_repository
import repositories.booking_repository as booking_repository

booking_blueprint = Blueprint("booking", __name__)

#INDEX
@booking_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

#NEW
@booking_blueprint.route("/bookings/new")
def new_booking():
    sessions = session_repository.select_all()
    students = student_repository.select_all()
    return render_template("bookings/new.html", sessions = sessions, students = students)

#NEW BOOKING FOR SELECTED SESSION
@booking_blueprint.route("/bookings/<id>/new")
def new_booking_for_selected_session(id):
    selected_session = session_repository.select(id)
    students = student_repository.select_all()
    return render_template("bookings/new_for_selected_session.html", selected_session = selected_session, students = students)

#CREATE
@booking_blueprint.route("/bookings", methods = ["POST"])
def create_booking():
    student_id = request.form["student_id"]
    session_id = request.form["session_id"]
    session = session_repository.select(session_id)
    student = student_repository.select(student_id)
    new_booking = Booking(student, session)
    booking_repository.save(new_booking)
    return redirect("/bookings")