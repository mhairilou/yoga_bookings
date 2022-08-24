from flask import Blueprint, Flask, redirect, render_template, request
from models.student import Student
from models.booking import Booking
import repositories.student_repository as student_repository
import repositories.booking_repository as booking_repository

student_blueprint = Blueprint("student", __name__)

#INDEX
@student_blueprint.route("/students")
def students():
    students = student_repository.select_all()
    return render_template("students/index.html", students=students)

# SHOW
@student_blueprint.route("/students/<id>")
def show_student(id):
    student = student_repository.select(id)
    bookings = booking_repository.select_all_bookings_by_student_id(id)
    return render_template("students/show.html", student = student, bookings = bookings)

#NEW
@student_blueprint.route("/students/new")
def new_student():
    return render_template("students/new.html")


#CREATE
@student_blueprint.route("/students", methods = ["POST"])
def create_student():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    credits = request.form["credits"]
    new_student = Student(first_name, last_name, credits)
    
    success = student_repository.save(new_student)
    if success:
        return redirect("/students/new/success")
    return redirect("/students/new/oops")

#CREATE OOPS
@student_blueprint.route("/students/new/oops", methods = ["GET"])
def create_student_fail():
    return render_template("students/new_oops.html")

#CREATE HOORAY
@student_blueprint.route("/students/new/success", methods = ["GET"])
def create_student_success():
    return render_template("students/new_success.html")


#EDIT
@student_blueprint.route("/students/<id>/edit")
def edit_student(id):
    student = student_repository.select(id)
    return render_template("students/edit.html", student = student)


#UPDATE
@student_blueprint.route("/students/<id>", methods = ["POST"])
def update_student(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    credits = request.form["credits"]
    student = Student(first_name, last_name, credits, id)
    student_repository.update(student)
    return render_template("students/show.html", student = student)
    
#DELETE
@student_blueprint.route("/students/<id>/delete", methods = ["POST"])
def delete_student(id):
    student_repository.delete(id)
    return redirect("/students")