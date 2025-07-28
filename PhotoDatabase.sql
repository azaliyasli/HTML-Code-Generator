CREATE DATABASE webphotos;

USE webphotos;

CREATE TABLE photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    photo_url VARCHAR(255),
    photo_file LONGBLOB,
    created_at DATETIME
);



