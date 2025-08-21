-- show databases;

-- create database university;

-- use university

-- CREATE TABLE students (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     fname VARCHAR(10) NOT NULL,
--     lname VARCHAR(10) NOT NULL,
--     age INT NOT NULL,
--     sex ENUM('male', 'female'),
--     email VARCHAR(50) NOT NULL UNIQUE,
--     is_active BOOLEAN DEFAULT TRUE
-- );

select * from students;

-- insert into students(fname, lname, age, sex, email, is_active) values
-- 	('Zunaira', 'Aslam', 23, 'female', 'zunaira@gmail.com', true),
--     ('Fiza', 'Arshad', 30, 'female', 'fiza@gmail.com', true),
--     ('Haroon', 'Aslam', 26, 'male', 'haroon@gmail.com', false);

-- select concat(fname," ",lname)  from students where is_active =true;
 
-- select * from students where lname like "A%";

-- alter table students drop column email;

-- select count(is_active) from students as total_count where is_active = true;

alter table students  are equal