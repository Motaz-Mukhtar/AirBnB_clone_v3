-- prepare MySQL server
-- Create hbnb_test_db database
-- create User hbnb_test@localhost and Grant all privileges on the
-- hbnb_test_db database and SELECT on performance_schema
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

CREATE USER
	IF NOT EXISTS 'hbnb_test'@'localhost'
	IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES
	ON `hbnb_test_db`.*
	TO 'hbnb_test'@'localhost';
GRANT SELECT
	ON `performance_schema`.*
	TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
