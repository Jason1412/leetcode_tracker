-- Last updated: 5/16/2026, 12:27:26 PM
# Write your MySQL query statement below
select distinct s1.*
from 
    stadium as s1,
    stadium as s2,
    stadium as s3
where 
    s1.people >= 100
    and s2.people >= 100
    and s3.people >= 100
    and ((s1.id - s2.id = -1 and s1.id - s3.id = -2 and s2.id - s3.id = -1) or /*t1 t2 t3*/
         (s1.id - s2.id = 1 and s1.id - s3.id = -1 and s2.id - s3.id = -2) or  /*t2 t1 t3 */
         /* (s1.id - s3.id = -1 and s3.id - s2.id = 1 and s1.id - s2.id = -2) or  t2 t3 t1*/
         (s3.id - s2.id = -1 and s2.id - s1.id = -1 and s3.id - s1.id = -2) /*or t3 t2 t1 */
         /* (s1.id - s2.id = -2 and s1.id - s3.id = -1 and s3.id - s2.id = -1) or t1 t3 t2 */
         /*(s3.id - s1.id = -1 and s1.id - s2.id = -1 and s3.id - s2.id = -1)    /*t3 t1 t2*/
    )
order by s1.id