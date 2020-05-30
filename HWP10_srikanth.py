"""python progeam to crete database of stevens students and instructors and majors
    author sikanth"""
import os
from prettytable import PrettyTable
from collections import defaultdict
import unittest


def file_read(path, num_fields, seperator=','or'|'or'*', header=False):
    try:
        fp = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(" cant find open the file: ", path)
    else:
        with fp:
            for n, line in enumerate(fp):
                if n == 0 and header:
                    continue  # skip header row
                else:
                    fields = line.strip()
                    fields = fields.split(seperator)
                    if len(fields) != num_fields:
                        raise ValueError(
                            "number of fields in the file is not equal to expected numnber of fields")
                    else:
                        yield fields


class Student:

    def __init__(self, cwid, name, major_name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._course = dict()  # _course[course]=grade
        self._major_name = major_name

    def add_course(self, course, grade):
        self._course[course] = grade

    def pt_row(self):
        completed_courses, remaining_requried_course, remaining_elective_course = self._major.grade_check(
            self._course)
        return[self._cwid, self._name, self._major_name, list(sorted(completed_courses)), remaining_requried_course, remaining_elective_course]


class Instructor:

    def __init__(self, cwid, name, dept):
        self._cwid = cwid
        self._name = name
        self.dept = dept
        self.course = defaultdict(int)

    def add_course(self, course):
        self.course[course] += 1

    def pt_row(self):
        for cr, st in self.course.items():
            yield [self._cwid, self._name, self.dept, cr, st]


class major:
    def __init__(self, name, passing=None):
        self._name = name
        self._requried = set()
        self._electives = set()
        self._passing_grade = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def pt_row(self):
        return[self._name, self._requried, self._electives]

    def add_course(self, flag, course):
        if flag == 'E':
            self._electives.add(course)
        elif flag == 'R':
            self._requried.add(course)
        else:
            raise ValueError(
                "value error forund unexpected flag in majors file")

    def grade_check(self, courses):
        completed_courses = {
            course for course, grade in courses.items() if grade in self._passing_grade}
        remaining_requried_course = self._requried - completed_courses
        if len(self._electives.intersection(completed_courses)) >= 1:
            remaining_elective_course = None
        else:
            remaining_elective_course = self._electives

        return[completed_courses, remaining_requried_course, remaining_elective_course]


class Repository:
    def __init__(self, path_dir):
        self.path_dir = path_dir
        self._students = dict()
        self._instructors = dict()
        self._major = dict()

        self.read_instructors(os.path.join(path_dir, "instructors.txt"))
        self.read_major(os.path.join(path_dir, "majors.txt"))
        self.read_students(os.path.join(path_dir, "students.txt"))
        self.read_grades(os.path.join(path_dir, "grades.txt"))

        self.major_table()
        self.student_table()
        self.instructor_table()

    def read_students(self, path_dir):
        try:
            for cwid, name, major in file_read(path_dir, 3, seperator='\t', header=False):
                if cwid in self._students:
                    print(f"cwid {cwid} already read from the file")
                else:
                    self._students[cwid] = Student(
                        cwid, name, major, self._major[major])
        except ValueError:
            print("value error")

    def read_instructors(self, path_dir):
        try:
            for cwid, name, dept in file_read(path_dir, 3, seperator='\t', header=False):
                if cwid in self._instructors:
                    print(f"cwid {cwid} already read from the list")
                else:
                    self._instructors[cwid] = Instructor(cwid, name, dept)
        except ValueError:
            print("value error")

    def read_grades(self, path_dir):
        for student_cwid, course, grade, instructor_cwid in file_read(path_dir, 4, seperator='\t', header=False):

            if student_cwid in self._students:
                self._students[student_cwid].add_course(course, grade)
            else:
                print(f"student cwid {student_cwid} not in the student file")

            if instructor_cwid in self._instructors:
                self._instructors[instructor_cwid].add_course(course)
            else:
                print(f"student cwit {instructor_cwid} not in file")

    def read_major(self, path_dir):
        try:
            for dept, requried, electives in file_read(path_dir, 3, seperator='\t', header=False):
                if dept in self._major:
                    self._major[dept].add_course(requried, electives)
                else:
                    self._major[dept] = major(dept)
                    self._major[dept].add_course(requried, electives)
        except ValueError:
            print("value error: ")

    def major_table(self):
        pt = PrettyTable(
            field_names=['major', 'requried course', 'elective course'])
        for major in self._major.values():
            pt.add_row(major.pt_row())
        print(pt)

    def student_table(self):
        pt = PrettyTable(
            field_names=['cwid', 'name', 'major', 'completed', 'remaining', 'elective'])
        for Student in self._students.values():
            pt.add_row(Student.pt_row())
        print("student pretty table")
        print(pt)

    def instructor_table(self):
        pt = PrettyTable(
            field_names=['cwid', 'name', 'dept', 'course', 'students'])
        for Instructor in self._instructors.values():
            for course in Instructor.pt_row():
                pt.add_row(course)
        print("instructor pretty table")
        print(pt)


def main():
    path_dir = "D:\\college\\ssw 810\\repo\\"
    #path_dir=input("enter the path directory: ")
    stevens = Repository(path_dir)


class RepositoryTest(unittest.TestCase):
    def test_stevens(self):
        path_dir = "D:\\college\\ssw 810\\repo\\"
        stevens = Repository(path_dir)
        student = [["10103", "Baldwin, C", "SFEN", ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, None],
                        ["10115", "Wyatt, X", "SFEN", ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, None],
                        ["10172", "Forbes, I", "SFEN", ['SSW 555', 'SSW 567'], {'SSW 564', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}],
                        ["10175", "Erickson, D", "SFEN", ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 555', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}],
                        ["10183", "Chapman, O", "SFEN", ['SSW 689'], {'SSW 567', 'SSW 555', 'SSW 564', 'SSW 540'}, {'CS 545', 'CS 501', 'CS 513'}],
                        ["11399", "Cordova, I", "SYEN", ['SSW 540'], {'SYS 612', 'SYS 800', 'SYS 671'}, None],
                        ["11461", "Wright, U", "SYEN", ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
                        ["11658", "Kelly, P", "SYEN", [], {'SYS 800', 'SYS 612', 'SYS 671'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
                        ["11714", "Morton, A", "SYEN", ['SYS 611', 'SYS 645'], {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 565', 'SSW 540', 'SSW 810'}],
                        ["11788", "Fuller, E", "SYEN", ['SSW 540'], {'SYS 671', 'SYS 612', 'SYS 800'}, None]]
        instructor = [["98765", "Einstein, A", "SFEN", "SSW 567", 4],
        ["98765", "Einstein, A", "SFEN", "SSW 540", 3],
         ["98764", "Feynman, R", "SFEN", "SSW 564", 3],
         ["98764", "Feynman, R", "SFEN", "SSW 687", 3],
         ["98764", "Feynman, R", "SFEN", "CS 501", 1],
         ["98764", "Feynman, R", "SFEN", "CS 545", 1],
         ["98763", "Newton, I", "SFEN", "SSW 555", 1],
         ["98763", "Newton, I", "SFEN", "SSW 689", 1],
         ["98760", "Darwin, C", "SYEN", "SYS 800", 1],
         ["98760", "Darwin, C", "SYEN", "SYS 750", 1],
         ["98760", "Darwin, C", "SYEN", "SYS 611", 2],
         ["98760", "Darwin, C", "SYEN", "SYS 645", 1]]

        major = [["SFEN", {'SSW 540', 'SSW 564', 'SSW 567', 'SSW 555'}, {'CS 545', 'CS 501', 'CS 513'}], ["SYEN", {'SYS 612', 'SYS 800', 'SYS 671'}, {'SSW 810', 'SSW 565', 'SSW 540'}]]

        ptstudent = [s.pt_row() for s in stevens._students.values()]
        ptinstructor = [row for Instructor in stevens._instructors.values() for row in Instructor.pt_row()]
        ptmajor = [m.pt_row() for m in stevens._major.values()]

        self.assertEqual(ptmajor, major)
        self.assertEqual(ptstudent, student)
        self.assertEqual(ptinstructor, instructor)


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)
