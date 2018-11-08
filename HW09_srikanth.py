"""python progeam to crete database of stevens students and instructors
    author sikanth"""
import os
from prettytable import PrettyTable
from collections import defaultdict
import unittest


def file_read(path, num_fields, seperator=',', header=False):
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
    def __init__(self, cwid, name, major):
        self._cwid = cwid
        self._name = name
        self._major = major
        self._course = dict()  # _course[course]=grade

        #self.lable=["CWID", "Name", "Major", "Courses"]

    def add_course(self, course, grade):
        self._course[course] = grade

    def pt_row(self):
        return[self._cwid, self._name, self._major, sorted(self._course.keys())]

    def __str__(self):
        return f"student: {self._cwid}  name: {self._name}  major: {self._major}  courses: {sorted(self._course.keys())}"


class Instructor:
    #pt_lable= ["CWID", "name", "departmant","Courses","students"]
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


class Repository:
    def __init__(self, path_dir):
        self.path_dir = path_dir
        self._students = dict()
        self._instructors = dict()

        #path_dir="D:\\college\\ssw 810\\repo\\"
        self.read_students(os.path.join(path_dir, "students.txt"))
        self.read_instructors(os.path.join(path_dir, "instructors.txt"))
        self.read_grades(os.path.join(path_dir, "grades.txt"))
        self.student_table()
        self.instructor_table()

    def read_students(self, path_dir):
        try:
            for cwid, name, major in file_read(path_dir, 3, seperator='\t', header=False):
                if cwid in self._students:
                    print(f"cwid {cwid} already read from the file")
                else:
                    self._students[cwid] = Student(cwid, name, major)
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

    def student_table(self):
        pt = PrettyTable(
            field_names=['cwid', 'name', 'major', 'completed course'])
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


class RepositoryTest(unittest.TestCase):
    def test_repository(self):
        path_dir = "D:\\college\\ssw 810\\repo\\"
        stevens = Repository(path_dir)
        expect_student = [["10103", "Baldwin, C", "SFEN", ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                          ["10115", "Wyatt, X", "SFEN", [
                              'CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                          ["10172", "Forbes, I", "SFEN", ['SSW 555', 'SSW 567']],
                          ["10175", "Erickson, D", "SFEN", [
                              'SSW 564', 'SSW 567', 'SSW 687']],
                          ["10183", "Chapman, O", "SFEN", ['SSW 689']],
                          ["11399", "Cordova, I", "SYEN", ['SSW 540']],
                          ["11461", "Wright, U", "SYEN", [
                              'SYS 611', 'SYS 750', 'SYS 800']],
                          ["11658", "Kelly, P", "SYEN", ['SSW 540']],
                          ["11714", "Morton, A", "SYEN", ['SYS 611', 'SYS 645']],
                          ["11788", "Fuller, E", "SYEN", ['SSW 540']]]
        expect_instructor = [["98765", "Einstein, A", "SFEN", "SSW 567", 4],
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

        student = [s.pt_row() for s in stevens._students.values()]
        instructor = [row for Instructor in stevens._instructors.values()
                      for row in Instructor.pt_row()]

        self.assertEqual(student, expect_student)
        self.assertEqual(instructor, expect_instructor)


def main():
    path_dir = "D:\\college\\ssw 810\\repo\\"
    #path_dir=input("enter the path directory: ")
    stevens = Repository(path_dir)


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)
