from flask import Blueprint, Flask, redirect, render_template, request
from models.booking import Booking
import repositories.session_repository as session_repository
import repositories.student_repository as student_repository
import repositories.booking_repository as booking_repository

booking_blueprint = Blueprint("booking", __name__)

#INDEX
@booking_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)