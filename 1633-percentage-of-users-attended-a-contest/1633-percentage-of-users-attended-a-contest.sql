# Write your MySQL query statement below
SELECT *
FROM
(
    SELECT
        contest_id,
        ROUND(COUNT(user_id) / (SELECT COUNT(*) FROM users) * 100, 2) percentage
    FROM register
    GROUP BY contest_id
) AS c
ORDER BY percentage DESC, contest_id ASC