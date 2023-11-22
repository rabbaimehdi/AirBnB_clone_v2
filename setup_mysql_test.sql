-- script prepares a MySQL server for the project
-- create hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- new user named : hbnb_test  with all privileges
-- with the password : hbnb_test_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting the SELECT privilege on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- granting all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
