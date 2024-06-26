-- Create the database exampledb if it doesn't already exist
CREATE DATABASE exampledb;

-- Switch to the exampledb database
\c exampledb

-- Create the example_table with some example columns
CREATE TABLE IF NOT EXISTS example_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    email VARCHAR(255)
);

-- Insert some example data into the example_table
INSERT INTO example_table (name, age, email) VALUES 
('Alice', 30, 'alice@example.com'),
('Bob', 25, 'bob@example.com'),
('Charlie', 35, 'charlie@example.com'),
('Diana', 28, 'diana@example.com');

-- Verify the data
SELECT * FROM example_table;
