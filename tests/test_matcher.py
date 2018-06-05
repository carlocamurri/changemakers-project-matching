import unittest

import src.matcher as matcher
from src.student import Student


class MatcherTest(unittest.TestCase):

    def test_matches_one_student_and_one_project(self):
        student = Student(1, [1])
        matcher.match([student])
        self.assertEqual(student.project, 1)

    def test_each_student_is_prioritized(self):
        student_1 = Student(1, [1, 2, 3])
        student_2 = Student(2, [2, 1, 3])
        student_3 = Student(3, [3, 1, 2])
        matcher.match([student_1, student_2, student_3])
        self.assertEqual(student_1.project, 1)
        self.assertEqual(student_2.project, 2)
        self.assertEqual(student_3.project, 3)

    '''
    def test_student_with_highest_grade_is_prioritized(self):
        student_1 = Student(1, [1, 2], grade=10)
        student_2 = Student(2, [1, 2], grade=7)
        matcher.match([student_1, student_2])
        self.assertEqual(student_1.project, 1)
        self.assertEqual(student_1.project, 2)
    '''

    def test_everyone_matched_is_stable(self):
        student_1 = Student(1, [1, 2])
        student_2 = Student(2, [2, 1])
        students = [student_1, student_2]
        matcher.match(students)
        self.assertTrue(matcher.is_stable(students))

    def test_some_unmatched_is_unstable(self):
        student_1 = Student(1, [1, 2])
        student_2 = Student(2, [2, 1])
        students = [student_1, student_2]
        self.assertFalse(matcher.is_stable(students))

    def test_some_matched_none_is_unstable(self):
        student_1 = Student(1, [1, 2])
        student_2 = Student(2, [2, 1])
        student_1.project = None
        students = [student_1, student_2]
        self.assertFalse(matcher.is_stable(students))

    def test_all_projects_are_available_at_beginning(self):
        student_1 = Student(1, [1, 2, 3])
        student_2 = Student(2, [2, 1, 3])
        student_3 = Student(3, [3, 1, 2])
        self.assertEqual( \
            matcher.get_available_projects([student_1, student_2, student_3]), \
            set([1, 2, 3]) \
        )

    def test_not_all_projects_are_available_if_one_is_taken(self):
        student_1 = Student(1, [1, 2, 3])
        student_2 = Student(2, [2, 1, 3])
        student_3 = Student(3, [3, 1, 2])
        student_2.project = 2
        self.assertEqual( \
            matcher.get_available_projects([student_1, student_2, student_3]), \
            set([1, 3]) \
        )
