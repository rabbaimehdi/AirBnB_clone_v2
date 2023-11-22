-- script prepares a MySQL server for the project
-- create hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- new user named : hbnb_dev  with all privileges
-- with the password : hbnb_dev_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- granting the SELECT privilege on the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting all privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
