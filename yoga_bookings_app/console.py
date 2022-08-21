import imp
from models.session import Session

import repositories.session_repository as session_repository

session1 = Session("Yin Yang", 90)

session_repository.save(session1)
