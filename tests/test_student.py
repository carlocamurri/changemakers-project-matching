import unittest

from src.entities.student import Student


class ProjectMock:

    def __init__(self):
        self.student = None


class StudentTest(unittest.TestCase):

    def test_student_is_matched_with_project(self):
        student = Student(1, [ProjectMock()])
        student.project = 1
        self.assertTrue(student.is_matched)

    def test_student_is_unmatched(self):
        student = Student(1, [ProjectMock()])
        self.assertFalse(student.is_matched)

    def test_grade_cannot_be_larger_than_ten(self):
        self.assertRaises(ValueError, Student, 1, [ProjectMock()], grade=13)

    def test_grade_cannot_be_less_than_zero(self):
        self.assertRaises(ValueError, Student, 1, [ProjectMock()], grade=-2)
