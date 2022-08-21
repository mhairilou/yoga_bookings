DROP TABLE IF EXISTS sessions;

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    yoga_type VARCHAR(255),
    duration INT
);
