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
def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for result in results:
        session = Session(result["yoga_type"], result["duration"], result["id"])
        sessions.append(session)
    return sessions

# SELECT BY ID


# DELETE ALL
def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

# DELETE BY ID


# UPDATE BY ID



