DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS students;

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    yoga_type VARCHAR(255),
    duration INT,
    date DATE NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    credits INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    student_id SERIAL NOT NULL REFERENCES students(id),
    session_id SERIAL NOT NULL REFERENCES sessions(id) ON delete cascade

);
