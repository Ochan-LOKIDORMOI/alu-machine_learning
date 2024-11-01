-- A script that creates a table with unique id, email and name columns
CREATE TABLE
    IF NOT EXISTS users (
        id INT NOT Null AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255)
    );
