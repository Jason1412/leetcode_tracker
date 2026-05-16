-- Last updated: 5/16/2026, 12:27:23 PM
# Write your MySQL query statement below
Select id, movie, description, rating
From cinema
Where id % 2 = 1 AND NOT description = 'boring'
Order by rating DESC