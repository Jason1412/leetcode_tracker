-- Last updated: 5/16/2026, 12:29:09 PM
# Write your MySQL query statement below
SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (SELECT CustomerId FROM Orders)
