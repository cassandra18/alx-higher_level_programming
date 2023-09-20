-- Creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges to the user user_0d_1 on all databases and tables.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1pwd'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Flush privileges to apply the changes.
FLUSH PRIVILEGES;
