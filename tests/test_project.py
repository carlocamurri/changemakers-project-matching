import unittest

from src.project import Project


class ProjectTest(unittest.TestCase):

    def test_project_is_matched_with_student(self):
        project = Project(1)
        project.student = 'a_student'
        self.assertTrue(project.is_matched())

    def test_project_is_unmatched(self):
        project = Project(1)
        self.assertFalse(project.is_matched())
