import imp
from models.session import Session

import repositories.session_repository as session_repository

session1 = Session("Yin Yang", 90)
session2 = Session("Hatha", 60)
session3 = Session("Vinyasa", 60)
session4 = Session("Restorative", 75)


session_repository.delete_all()

session_repository.save(session1)
session_repository.save(session2)
session_repository.save(session3)
session_repository.save(session4)



