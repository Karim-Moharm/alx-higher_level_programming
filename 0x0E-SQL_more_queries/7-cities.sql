-- creates the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),

	CONSTRAINT cities_PK PRIMARY KEY (cities.id),
	CONSTRAINT state_cities_FK FOREIGN KEY (state_id)
	REFERENCES state (state.id)
);
