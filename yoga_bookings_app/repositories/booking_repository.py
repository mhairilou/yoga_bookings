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