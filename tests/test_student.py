import unittest

from utils import create_student

from src.student import Student


class ProjectMock:

    def __init__(self):
        self.student = None


class StudentTest(unittest.TestCase):

    def test_student_is_matched_with_project(self):
        student = Student(1, [ProjectMock()])
        student.project = 1
        self.assertTrue(student.is_matched())

    def test_student_is_not_matched_when_unmatched(self):
        student = Student(1, [ProjectMock()])
        self.assertFalse(student.is_matched())

    def test_pair_matches_student_with_project(self):
        project = ProjectMock()
        student = Student(1, [project])
        student.pair(project)
        self.assertEqual(student.project, project)
        self.assertEqual(project.student, student) 

    def test_unpairing_student_with_project(self):
        project = ProjectMock()
        student = Student(1, [project])
        student.pair(project)
        student.unpair()
        self.assertIsNone(student.project)
        self.assertIsNone(project.student)
