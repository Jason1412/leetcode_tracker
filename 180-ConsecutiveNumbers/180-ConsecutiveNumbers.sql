-- Last updated: 5/16/2026, 12:29:12 PM
# Write your MySQL query statement below
Select 
    distinct(l1.num) as ConsecutiveNums
from 
    Logs as l1,
    Logs as l2,
    Logs as l3
Where
    l1.id = l2.id - 1
    AND l2.id = l3.id - 1
    AND l1.Num = l2.Num
    And l2.Num = l3.Num
    