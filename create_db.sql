CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    date DATE,
    location VARCHAR(100),
    quota INT
);

CREATE TABLE participants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    event_id INT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);
