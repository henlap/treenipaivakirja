CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    done_at TEXT,
    sent_at TIMESTAMP

);

CREATE TABLE movements (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE movement_in_workout (
    id SERIAL PRIMARY KEY,
    movement_id INTEGER REFERENCES movements,
    workout_id INTEGER REFERENCES workouts
);

CREATE TABLE sets (
    id SERIAL PRIMARY KEY,
    movement_in_workout_id INTEGER REFERENCES movement_in_workout,
    repetitions INTEGER,
    weight_used INTEGER,
    rpe INTEGER
);

