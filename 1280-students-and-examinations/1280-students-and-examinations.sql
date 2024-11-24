# Write your MySQL query statement below
SELECT 
    students.student_id,
    student_name,
    subjects.subject_name,
    COUNT(examinations.student_id) attended_exams
FROM students
CROSS JOIN subjects
LEFT JOIN examinations
    ON examinations.subject_name = subjects.subject_name
    AND students.student_id = examinations.student_id
GROUP BY student_name, subjects.subject_name
ORDER BY students.student_id, subjects.subject_name