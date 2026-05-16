-- Last updated: 5/16/2026, 12:29:10 PM
# Write your MySQL query statement below
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Id) > 1;