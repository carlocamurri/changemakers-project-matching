import unittest

from src.pair import PairFactory


STUDENT = 'A Student'
PROJECT = 'A Project'


class PairTest(unittest.TestCase):

    def setUp(self):
        factory = PairFactory()
        self.pair = factory.create(STUDENT, PROJECT)

    def test_creates_pair_with_correct_student(self):
        self.assertEqual(self.pair.student, STUDENT)

    def test_creates_pair_with_correct_project(self):
        self.assertEqual(self.pair.project, PROJECT)
