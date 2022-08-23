from db.run_sql import run_sql

from models.booking import Booking
from models.session import Session
from models.student import Student

import repositories.session_repository as session_repository
import repositories.student_repository as student_repository

# SAVE
def save(booking):
    sql = "INSERT INTO bookings (student_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [booking.student.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id

# SELECT ALL
def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        student = student_repository.select(result["student_id"])
        session = session_repository.select(result["session_id"])
        booking = Booking(student, session, result["id"])
        bookings.append(booking)
    return bookings

# SELECT ALL BOOKINGS BY SESSION ID
def select_all_bookings_by_session_id(session_id):
    bookings = []
    sql = "SELECT * FROM bookings WHERE session_id = %s"
    values = [session_id]
    results = run_sql(sql, values)
    for result in results:
        session = session_repository.select(result["session_id"])  
        student = student_repository.select(result["student_id"])      
        booking = Booking(student, session, result["id"])
        bookings.append(booking)
    return bookings

# SELECT ALL BOOKINGS BY STUDENT ID
def select_all_bookings_by_student_id(student_id):
    bookings = []
    sql = "SELECT * FROM bookings WHERE student_id = %s"
    values = [student_id]
    results = run_sql(sql, values)
    for result in results:
        session = session_repository.select(result["session_id"])  
        student = student_repository.select(result["student_id"])      
        booking = Booking(student, session, result["id"])
        bookings.append(booking)
    return bookings


# DELETE ALL
def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)