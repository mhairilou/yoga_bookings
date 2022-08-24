from db.run_sql import run_sql

from models.student import Student

# SAVE
def save(student):
    sql = "INSERT INTO students (first_name, last_name, credits) VALUES (%s, %s, %s) RETURNING id"
    values = [student.first_name, student.last_name, student.credits]
    results = run_sql(sql, values)

   
    if len(results) == 0:
        return False

    id = results[0]['id']
    student.id = id
    return True

# SELECT ALL
def select_all():
    students = []
    sql = "SELECT * FROM students"
    results = run_sql(sql)
    for result in results:
        student = Student(result["first_name"], result["last_name"], result["credits"], result["id"])
        students.append(student)
    return students

# SELECT BY ID
def select(id):
    sql = "SELECT * FROM students WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        student = Student(result["first_name"], result["last_name"], result["credits"], result["id"])
        return student

# DELETE ALL
def delete_all():
    sql = "DELETE FROM students"
    run_sql(sql)


# DELETE BY ID
def delete(id):
    sql = "DELETE FROM students WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# UPDATE BY ID
def update(student):
    sql = "UPDATE students SET (first_name, last_name, credits) = (%s, %s, %s) WHERE id = %s"
    values = [student.first_name, student.last_name, student.credits, student.id]
    run_sql(sql, values)
    



