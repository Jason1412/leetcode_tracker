-- Last updated: 5/16/2026, 12:29:07 PM
# Write your MySQL query statement below
Select Department.Name as Department, Employee.Name as Employee, Employee.Salary
From Employee
Inner Join Department on Employee.DepartmentId = Department.Id
Where
(Employee.DepartmentId, Salary) IN
(Select
    DepartmentId, Max(Salary)
From
    Employee
Group by DepartmentId)