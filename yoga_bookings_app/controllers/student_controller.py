from flask import Blueprint, Flask, redirect, render_template, request
from models.student import Student
import repositories.student_repository as student_repository

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
    return render_template("students/show.html", student = student)

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
    student_repository.save(new_student)
    return redirect("/students")


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
    student = Student(first_name, last_name, credits)
    student_repository.update(student)
    return redirect("/students/<id>")

#DELETE
@student_blueprint.route("/students/<id>/delete", methods = ["POST"])
def delete_student(id):
    student_repository.delete(id)
    return redirect("/students")