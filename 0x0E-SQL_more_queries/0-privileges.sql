-- list all privileges for users: user_0d_1 and user_0d_2 on the server

SELECT user,host FROM mysql.user;

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
