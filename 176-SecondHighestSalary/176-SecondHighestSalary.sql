-- Last updated: 5/16/2026, 12:29:14 PM
# Write your MySQL query statement below
SELECT max(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee);