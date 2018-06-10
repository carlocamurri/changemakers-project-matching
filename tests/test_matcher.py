import unittest
import sys
import logging

from src.matcher import Matcher
from src.student import Student
from src.project import Project


class MatcherTest(unittest.TestCase):

    def setUp(self):
        self.p_1 = Project(1)
        self.p_2 = Project(2)
        self.p_3 = Project(3)

    def create_sample_students(self, n):
        projects = [Project(i) for i in range(1, n + 1)]
        students = [Student(i, projects) for i in range(1, n + 1)]
        return students, projects

    def assert_students_higher_priority_are_prioritized(self, students, projects):
        for i, student in enumerate(students):
            self.assertEqual(student.project, projects[-(i + 1)])

    def test_matches_one_student_and_one_project(self):
        student = Student(1, [self.p_1])
        matcher = Matcher([student])
        matcher.match()
        self.assertEqual(student.project, self.p_1)

    def test_each_student_is_prioritized(self):
        student_1 = Student(1, [self.p_1, self.p_2, self.p_3])
        student_2 = Student(2, [self.p_2, self.p_1, self.p_3])
        student_3 = Student(3, [self.p_3, self.p_1, self.p_2])
        matcher = Matcher([student_1, student_2, student_3])
        matcher.match()
        self.assertEqual(student_1.project, self.p_1)
        self.assertEqual(student_2.project, self.p_2)
        self.assertEqual(student_3.project, self.p_3)

    def test_everyone_matched_is_stable(self):
        student_1 = Student(1, [self.p_1, self.p_2])
        student_2 = Student(2, [self.p_2, self.p_1])
        students = [student_1, student_2]
        matcher = Matcher(students)
        matcher.match()
        self.assertTrue(matcher.is_stable())

    def test_some_unmatched_is_unstable(self):
        student_1 = Student(1, [self.p_1, self.p_2])
        student_2 = Student(2, [self.p_2, self.p_1])
        students = [student_1, student_2]
        matcher = Matcher(students)
        self.assertFalse(matcher.is_stable())

    def test_some_matched_none_is_unstable(self):
        student_1 = Student(1, [self.p_1, self.p_2])
        student_2 = Student(2, [self.p_2, self.p_1])
        student_1.project = None
        students = [student_1, student_2]
        matcher = Matcher(students)
        self.assertFalse(matcher.is_stable())

    def test_all_projects_are_available_at_beginning(self):
        student_1 = Student(1, [self.p_1, self.p_2, self.p_3])
        student_2 = Student(2, [self.p_2, self.p_1, self.p_3])
        student_3 = Student(3, [self.p_3, self.p_1, self.p_2])
        students = [student_1, student_2, student_3]
        matcher = Matcher(students)
        self.assertEqual( \
            matcher.get_available_projects(), \
            set([self.p_1, self.p_2, self.p_3]) \
        )

    def test_not_all_projects_are_available_if_one_is_taken(self):
        student_1 = Student(1, [self.p_1, self.p_2, self.p_3])
        student_2 = Student(2, [self.p_2, self.p_1, self.p_3])
        student_3 = Student(3, [self.p_3, self.p_1, self.p_2])
        student_2.project = self.p_2
        students = [student_1, student_2, student_3]
        matcher = Matcher(students)
        self.assertEqual( \
            matcher.get_available_projects(), \
            set([self.p_1, self.p_3]) \
        )

    def test_get_all_unmatched_students(self):
        student_1 = Student(1, [self.p_1, self.p_2, self.p_3])
        student_2 = Student(2, [self.p_2, self.p_1, self.p_3])
        student_3 = Student(3, [self.p_3, self.p_1, self.p_2])
        students = [student_1, student_2, student_3]
        matcher = Matcher(students)
        student_1.project = self.p_1
        student_2.project = None
        self.assertEqual(set(matcher.get_unmatched_students()), set([student_2, student_3]))

    def test_pair_student_project(self):
        student = Student(1, [self.p_1])
        matcher = Matcher([student])
        matcher.pair(student, self.p_1)
        self.assertEqual(student.project, self.p_1)

    def test_student_with_highest_priority_is_prioritized(self):
        student_1 = Student(1, [self.p_1, self.p_2])
        student_2 = Student(2, [self.p_1, self.p_2])
        def priority(student, project):
            return 2 if student == student_1 else 1
        matcher = Matcher([student_1, student_2], priority)
        matcher.match()
        self.assertEqual(student_1.project, self.p_1)
        self.assertEqual(student_2.project, self.p_2)

    def test_students_with_higher_priority_are_prioritized_in_order(self):
        students, projects = self.create_sample_students(40)
        def many_students_priority_calculator(student, project):
            return students.index(student) + 1
        matcher = Matcher(students, many_students_priority_calculator)
        matcher.match()
        self.assert_students_higher_priority_are_prioritized(students, projects)
