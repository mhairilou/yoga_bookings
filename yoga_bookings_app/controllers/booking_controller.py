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
@booking_blueprint.route("/bookings/{{session.id}}/new")
def new_booking():
    session = session_repository.select_all()
    student = student_repository.select_all()
    return render_template("bookings/new.html", sessions = sessions, students = students)

#CREATE
@booking_blueprint.route("/bookings", methods = ["POST"])
def create_booking():
    student = request.form["student"]
    session = request.form["session"]
    new_booking = Booking(student, session, id)
    booking_repository.save(new_booking)
    return redirect("/bookings")