-- create table called `second_table`
-- add some info to it

CREATE TABLE IF NOT EXISTS second_table (
	id,
	name VARCHAR(256),
	score INT
);

INSERT INTO second_table
VALUES (id, name, score) (1, 'John', 10),
			 (2, 'Alex', 3),
			 (3, 'Bob', 14),
			 (4, 'Georage', 8);
