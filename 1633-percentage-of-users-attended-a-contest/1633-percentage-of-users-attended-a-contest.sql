# Write your MySQL query statement below
WITH user_count AS (
    SELECT COUNT(*) 
    FROM users
)
SELECT *
FROM
(
    SELECT
        contest_id,
        ROUND(COUNT(contest_id) / (SELECT * FROM user_count) * 100, 2) percentage
    FROM register
    GROUP BY contest_id
) AS c
ORDER BY percentage DESC, contest_id ASC