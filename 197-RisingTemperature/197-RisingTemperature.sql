-- Last updated: 5/16/2026, 12:29:03 PM
# Write your MySQL query statement below
SELECT E1.Id 
FROM Weather AS E1, Weather AS E2
WHERE E1.Temperature > E2.Temperature AND DATEDIFF(E1.Date, E2.Date) = 1