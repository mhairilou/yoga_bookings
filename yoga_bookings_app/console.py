from models.session import Session
from models.student import Student
from models.booking import Booking

import repositories.session_repository as session_repository
import repositories.student_repository as student_repository
import repositories.booking_repository as booking_repository

import datetime


session_repository.delete_all()

session1 = Session("Yin Yang", 90, datetime.datetime(2022, 12, 12))

session2 = Session("Hatha", 60, datetime.datetime(2022, 12, 12))
session3 = Session("Vinyasa", 60, datetime.datetime(2022, 12, 12))
session4 = Session("Restorative", 75, datetime.datetime(2022, 12, 12))


session_repository.save(session1)
session_repository.save(session2)
session_repository.save(session3)
session_repository.save(session4)

# session_repository.save(session2)
# session_repository.save(session3)
# session_repository.save(session4)

# session_repository.delete(session3.id)

session = session_repository.select(session1.id)

session1.duration= 100
session_repository.update(session1)

student1 = Student("Peppa", "Pig", 5)

student_repository.save(student1)

booking1 = Booking(student1, session1)

booking_repository.save(booking1)

