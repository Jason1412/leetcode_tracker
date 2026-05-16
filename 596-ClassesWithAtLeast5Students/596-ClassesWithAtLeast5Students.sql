-- Last updated: 5/16/2026, 12:27:28 PM
# Write your MySQL query statement below
select 
    class 
from 
    courses
group by class
having count(distinct student) >= 5
