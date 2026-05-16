-- Last updated: 5/16/2026, 12:29:15 PM
# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State
FROM Person
LEFT JOIN Address on Person.PersonID = Address.PersonID

