DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS students;

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    yoga_type VARCHAR(255),
    duration INT
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    credits INT
)
