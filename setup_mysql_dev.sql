-- prepare MySQL server
-- Create hbnb_dev_db database
-- create User hbnb_dev@localhost and Grant all privileges on the
-- hbnb_test_db database and SELECT on performance_schema
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

CREATE USER
	IF NOT EXISTS 'hbnb_dev'@'localhost'
	IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
	ON `hbnb_dev_db`.*
	TO 'hbnb_dev'@'localhost';
GRANT SELECT
	ON `performance_schema`.*
	TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
