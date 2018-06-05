import unittest

from utils import create_student

from src.student import Student

class StudentTest(unittest.TestCase):

    def test_student_is_matched_with_project(self):
        student = Student(1, [1])
        student.project = 1
        self.assertTrue(student.is_matched())

    def test_student_is_not_matched_when_unmatched(self):
        student = Student(1, [1])
        self.assertFalse(student.is_matched())
