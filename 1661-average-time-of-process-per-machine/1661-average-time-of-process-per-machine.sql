# Write your MySQL query statement below
SELECT 
    start.machine_id,
    ROUND(AVG(end.timestamp - start.timestamp), 3) processing_time
FROM activity start
INNER JOIN activity end
    ON start.machine_id = end.machine_id
    AND start.process_id = end.process_id
    AND start.activity_type != end.activity_type
    AND start.activity_type = 'start'
GROUP BY start.machine_id
