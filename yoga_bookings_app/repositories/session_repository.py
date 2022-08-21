from db.run_sql import run_sql

from models.session import Session

# SAVE
def save(session):
    sql = "INSERT INTO sessions (yoga_type, duration) VALUES (%s, %s) RETURNING id"
    values = [session.yoga_type, session.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id

# SELECT ALL


# SELECT BY ID


# DELETE ALL


# DELETE BY ID


# UPDATE BY ID



