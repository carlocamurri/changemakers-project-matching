import unittest

from src.project import Project
from src.supervisor import Supervisor


class ProjectTest(unittest.TestCase):

    def test_project_is_matched_with_student(self):
        project = Project(1)
        project.student = 'a_student'
        self.assertTrue(project.is_matched)

    def test_project_is_unmatched(self):
        project = Project(1)
        self.assertFalse(project.is_matched)

    def test_priority_split_obtained_from_supervisor(self):
        priority_split = 'a_split'
        supervisor = Supervisor(priority_split)
        project = Project(1, supervisor=supervisor)
        self.assertEqual(project.priority_split, supervisor.priority_split)
