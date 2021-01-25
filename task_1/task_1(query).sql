SELECT courses.name FROM courses
UNION
SELECT teachers.name FROM teachers;


SELECT teachers.id, teachers.name, count(*) as Highest
FROM courses
JOIN teachers on teachers.id=courses.teacher_id
GROUP BY teachers.id
ORDER BY Highest DESC;

SELECT id, name FROM teachers
WHERE id NOT IN (SELECT teacher_id from courses)