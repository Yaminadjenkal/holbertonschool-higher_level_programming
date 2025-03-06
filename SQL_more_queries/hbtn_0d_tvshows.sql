-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;

-- Use the created database
USE hbtn_0d_tvshows;

-- Disable foreign key checks to avoid constraints issues while dropping tables
SET FOREIGN_KEY_CHECKS = 0;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS tv_show_genres;
DROP TABLE IF EXISTS tv_genres;
DROP TABLE IF EXISTS tv_shows;

-- Enable foreign key checks back
SET FOREIGN_KEY_CHECKS = 1;

-- Create the tv_genres table
CREATE TABLE tv_genres (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

-- Insert data into tv_genres
INSERT INTO tv_genres (id, name)
VALUES 
(1, 'Drama'),
(2, 'Mystery'),
(3, 'Adventure'),
(4, 'Fantasy'),
(5, 'Comedy'),
(6, 'Crime'),
(7, 'Suspense'),
(8, 'Thriller');

-- Create the tv_shows table
CREATE TABLE tv_shows (
  id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB;

-- Insert data into tv_shows
INSERT INTO tv_shows (id, title)
VALUES 
(1, 'House'),
(2, 'Game of Thrones'),
(3, 'The Big Bang Theory'),
(4, 'New Girl'),
(5, 'Silicon Valley'),
(6, 'Breaking Bad'),
(7, 'Better Call Saul'),
(8, 'Dexter'),
(9, 'Homeland'),
(10, 'The Last Man on Earth');

-- Create the tv_show_genres table
CREATE TABLE tv_show_genres (
  show_id INT NOT NULL,
  genre_id INT NOT NULL,
  KEY show_id (show_id),
  KEY genre_id (genre_id),
  CONSTRAINT tv_show_genres_ibfk_1 FOREIGN KEY (show_id) REFERENCES tv_shows (id),
  CONSTRAINT tv_show_genres_ibfk_2 FOREIGN KEY (genre_id) REFERENCES tv_genres (id)
) ENGINE=InnoDB;

-- Insert data into tv_show_genres
INSERT INTO tv_show_genres (show_id, genre_id)
VALUES 
(1, 1), (1, 2),
(2, 3), (2, 1), (2, 4),
(3, 5),
(4, 5),
(5, 5),
(6, 6), (6, 1), (6, 7), (6, 8),
(8, 6), (8, 1), (8, 2), (8, 7), (8, 8),
(10, 5), (10, 1);

