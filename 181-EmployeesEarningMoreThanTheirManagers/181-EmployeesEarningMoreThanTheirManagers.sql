-- Last updated: 5/16/2026, 12:29:10 PM
# Write your MySQL query statement below
SELECT E1.Name AS Employee
FROM Employee AS E1, Employee AS E2
WHERE E1.Salary > E2.Salary AND E2.Id = E1.ManagerId;