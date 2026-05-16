-- Last updated: 5/16/2026, 12:29:13 PM
# Write your MySQL query statement below
select Score,
(select count(distinct Score) from Scores where Score>=s.Score) as Rank
from Scores as  s
order by Score desc