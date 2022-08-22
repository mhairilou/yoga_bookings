from models.session import Session
from models.student import Student

import repositories.session_repository as session_repository
import repositories.student_repository as student_repository

session1 = Session("Yin Yang", 90)
session2 = Session("Hatha", 60)
session3 = Session("Vinyasa", 60)
session4 = Session("Restorative", 75)


session_repository.delete_all()

session_repository.save(session1)
session_repository.save(session2)
session_repository.save(session3)
session_repository.save(session4)

session_repository.delete(session3.id)

session = session_repository.select(session1.id)
print(session.yoga_type)

session1.duration= 100
session_repository.update(session1)

student1 = Student("Peppa", "Pig", 5)

student_repository.save(student1)


