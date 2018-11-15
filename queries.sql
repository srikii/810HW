select NAME, CWID from students where CWID = '11461';

select Major, count(*) as total_students from students group by Major;

select Grade, count(Grade) as grade_count from grades group by Grade limit 1;

select s.NAME, s.CWID, s.Major, g.Course, g.grade from students s join grades g on s.CWID=g.Student_CWID;

select s.NAME, s.CWID, s.Major, g.Course, g.grade from students s join grades g on s.CWID=g.Student_CWID where g.course = 'SSW 540';

select i.NAME, i.CWID, i.Dept, g.Course, count(g.student_CWID) as total_students 
from instructors i join grades g on i.CWID=g.instructor_CWID group by i.cwid, g.course;