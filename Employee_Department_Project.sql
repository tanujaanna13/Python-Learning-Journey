-- ===========================================
-- Project: SQL 50 Commands Based on Two Tables
-- Database: SQL PLUS
-- Tables: Employee and Department
-- Author: Shaik Noorjahan
-- ===========================================


-- ==========================================================
-- PART 1: CREATE TABLES
-- ==========================================================


-- Create Department Table
CREATE TABLE Department (
    DeptID NUMBER PRIMARY KEY,
    DeptName VARCHAR2(30),
    Location VARCHAR2(30)
);

-- Insert Department Data
INSERT INTO Department VALUES (10,'HR','Delhi');
INSERT INTO Department VALUES (20,'IT','Bangalore');
INSERT INTO Department VALUES (30,'Finance','Mumbai');
INSERT INTO Department VALUES (40,'Marketing','Hyderabad');
INSERT INTO Department VALUES (50,'Sales','Pune');

COMMIT;

-- Create Employee Table
CREATE TABLE Employee (
    EmpID NUMBER PRIMARY KEY,
    EmpName VARCHAR2(30),
    Gender VARCHAR2(10),
    Experience NUMBER,
    DeptID NUMBER,
    Salary NUMBER,
    ManagerID NUMBER,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);


-- ==========================================================
-- PART 2: INSERT DATA
-- ==========================================================


-- Insert Employee Data
INSERT INTO Employee VALUES (101,'Amit','Male',5,10,50000,105);
INSERT INTO Employee VALUES (102,'Neha','Female',6,20,60000,106);
INSERT INTO Employee VALUES (103,'Ravi','Male',4,10,55000,105);
INSERT INTO Employee VALUES (104,'Priya','Female',8,30,65000,107);
INSERT INTO Employee VALUES (105,'Raj','Male',10,10,80000,NULL);
INSERT INTO Employee VALUES (106,'Simran','Female',9,20,85000,NULL);
INSERT INTO Employee VALUES (107,'Mohit','Male',12,30,90000,NULL);
INSERT INTO Employee VALUES (108,'Karan','Male',3,40,45000,107);

COMMIT;


-- ==========================================================
-- PART 3: BASIC SELECT QUERIES (Queries 1-10)
-- ==========================================================


-- Query 1: Display all employee details
SELECT * FROM Employee;

-- Query 2: Display only employee names
SELECT EmpName FROM Employee;

-- Query 3: Display employee names and salaries
SELECT EmpName, Salary FROM Employee;

-- Query 4: Display employee names and department IDs
SELECT EmpName, DeptID FROM Employee;

-- Query 5: Display all female employees
SELECT * FROM Employee WHERE Gender='Female';

-- Query 6: Display all male employees
SELECT * FROM Employee WHERE Gender='Male';

-- Query 7: Display employees whose salary is greater than 60000
SELECT * FROM Employee WHERE Salary > 60000;

-- Query 8: Display employees whose salary is less than 50000
SELECT * FROM Employee WHERE Salary < 50000;

-- Query 9: Display employees with more than 5 years of experience
SELECT * FROM Employee WHERE Experience > 5;

-- Query 10: Display employees working in department 10
SELECT * FROM Employee WHERE DeptID = 10;


-- ==========================================================
-- PART 4: WHERE, BETWEEN, LIKE & IN (Queries 11-20)
-- ==========================================================


-- Query 11: Display employees whose salary is between 50000 and 80000.
SELECT *
FROM Employee
WHERE Salary BETWEEN 50000 AND 80000;

-- Query 12: Display employees whose experience is between 3 and 7 years.
SELECT *
FROM Employee
WHERE Experience BETWEEN 3 AND 7;

-- Query 13: Display employees whose names start with 'A'.
SELECT *
FROM Employee
WHERE EmpName LIKE 'A%';

-- Query 14: Display employees whose names end with 'a'.
SELECT *
FROM Employee
WHERE EmpName LIKE '%a';

-- Query 15: Display employees whose names contain the letter 'r'.
SELECT *
FROM Employee
WHERE LOWER(EmpName) LIKE '%r%';

-- Query 16: Display employees who are not in Department 10.
SELECT *
FROM Employee
WHERE DeptID <> 10;

-- Query 17: Display employees whose salary is not equal to 70000.
SELECT *
FROM Employee
WHERE Salary <> 70000;

-- Query 18: Display employees who have exactly 5 years of experience.
SELECT *
FROM Employee
WHERE Experience = 5;

-- Query 19: Display employees whose names have exactly five characters.
SELECT *
FROM Employee
WHERE LENGTH(EmpName) = 5;

-- Query 20: Display employees whose Department ID is either 10 or 30.
SELECT *
FROM Employee
WHERE DeptID IN (10, 30);


-- ==========================================================
-- PART 5: ORDER BY (Queries 21-25)
-- ==========================================================


-- Query 21: Display all employees in ascending order of salary
SELECT *
FROM Employee
ORDER BY Salary ASC;

-- Query 22: Display all employees in descending order of salary
SELECT *
FROM Employee
ORDER BY Salary DESC;

-- Query 23: Display employees sorted by experience
SELECT *
FROM Employee
ORDER BY Experience ASC;

-- Query 24: Display employees sorted by name alphabetically
SELECT *
FROM Employee
ORDER BY EmpName ASC;

-- Query 25: Display employees sorted first by department and then by salary
SELECT *
FROM Employee
ORDER BY DeptID ASC, Salary ASC;


-- ==========================================================
-- PART 6: AGGREGATE FUNCTIONS (Queries 26-33)
-- ==========================================================


-- Query 26: Find the total number of employees
SELECT COUNT(*) AS Total_Employees
FROM Employee;

-- Query 27: Find the highest salary
SELECT MAX(Salary) AS Highest_Salary
FROM Employee;

-- Query 28: Find the lowest salary
SELECT MIN(Salary) AS Lowest_Salary
FROM Employee;

-- Query 29: Find the average salary
SELECT AVG(Salary) AS Average_Salary
FROM Employee;

-- Query 30: Find the total salary paid to all employees
SELECT SUM(Salary) AS Total_Salary
FROM Employee;

-- Query 31: Find the average experience of employees
SELECT AVG(Experience) AS Average_Experience
FROM Employee;

-- Query 32: Find the total number of female employees
SELECT COUNT(*) AS Total_Female_Employees
FROM Employee
WHERE Gender = 'Female';

-- Query 33: Find the total number of male employees
SELECT COUNT(*) AS Total_Male_Employees
FROM Employee
WHERE Gender = 'Male';


-- ==========================================================
-- PART 7: GROUP BY (Queries 34-40)
-- ==========================================================


-- Query 34: Count employees in each department
SELECT DeptID, COUNT(*) AS Total_Employees
FROM Employee
GROUP BY DeptID;

-- Query 35: Find the average salary of each department
SELECT DeptID, AVG(Salary) AS Average_Salary
FROM Employee
GROUP BY DeptID;

-- Query 36: Find the maximum salary in each department
SELECT DeptID, MAX(Salary) AS Maximum_Salary
FROM Employee
GROUP BY DeptID;

-- Query 37: Find the minimum salary in each department
SELECT DeptID, MIN(Salary) AS Minimum_Salary
FROM Employee
GROUP BY DeptID;

-- Query 38: Find the total salary of each department
SELECT DeptID, SUM(Salary) AS Total_Salary
FROM Employee
GROUP BY DeptID;

-- Query 39: Count male and female employees separately
SELECT Gender, COUNT(*) AS Total_Employees
FROM Employee
GROUP BY Gender;

-- Query 40: Find the average experience of each department
SELECT DeptID, AVG(Experience) AS Average_Experience
FROM Employee
GROUP BY DeptID;


-- ==========================================================
-- PART 8: HAVING CLAUSE (Queries 41-45)
-- ==========================================================


-- Query 41: Find departments having more than two employees
SELECT DeptID, COUNT(*) AS Total_Employees
FROM Employee
GROUP BY DeptID
HAVING COUNT(*) > 2;

-- Query 42: Find departments where the average salary is greater than 70000
SELECT DeptID, AVG(Salary) AS Average_Salary
FROM Employee
GROUP BY DeptID
HAVING AVG(Salary) > 70000;

-- Query 43: Find departments where the maximum salary exceeds 80000
SELECT DeptID, MAX(Salary) AS Maximum_Salary
FROM Employee
GROUP BY DeptID
HAVING MAX(Salary) > 80000;

-- Query 44: Find departments where the total salary is greater than 150000
SELECT DeptID, SUM(Salary) AS Total_Salary
FROM Employee
GROUP BY DeptID
HAVING SUM(Salary) > 150000;

-- Query 45: Find departments having exactly two employees
SELECT DeptID, COUNT(*) AS Total_Employees
FROM Employee
GROUP BY DeptID
HAVING COUNT(*) = 2;


-- ==========================================================
-- PART 9: SUBQUERIES & INTERVIEW QUESTIONS (Queries 46-50)
-- ==========================================================


-- Query 46: Find employees whose salary is greater than the average salary
SELECT *
FROM Employee
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employee
);

-- Query 47: Find employees having the maximum salary
SELECT *
FROM Employee
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employee
);

-- Query 48: Find employees having the minimum salary
SELECT *
FROM Employee
WHERE Salary = (
    SELECT MIN(Salary)
    FROM Employee
);

-- Query 49: Find employees earning more than Amit
SELECT *
FROM Employee
WHERE Salary > (
    SELECT Salary
    FROM Employee
    WHERE EmpName = 'Amit'
);

-- Query 50: Find the employee with the second-highest salary
SELECT *
FROM Employee
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employee
    WHERE Salary < (
        SELECT MAX(Salary)
        FROM Employee
    )
);



-- ==========================================================
-- END OF PROJECT
-- ==========================================================


