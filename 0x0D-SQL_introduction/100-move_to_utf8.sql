-- script that converts hbtn_0c_0 database to UTF8

USE hbtn_0c_0;

-- converting the table
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- convert the Field name
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
