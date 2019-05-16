import unittest

from src.gateways import StudentIsMatchedGateway, ProjectIsMatchedGateway, UnmatchedStudentsGateway


PAIRED_STUDENT = 'A Paired Student'
UNPAIRED_STUDENT = 'An Unpaired Student'
ANOTHER_UNPAIRED_STUDENT = 'Another Unmatched Student'

UNPAIRED_STUDENTS = [UNPAIRED_STUDENT, ANOTHER_UNPAIRED_STUDENT]

PAIRED_PROJECT = 'A Paired Project'
UNPAIRED_PROJECT = 'An Unpaired Project'

PAIR = 'A Pair'


class PairRepositoryStub:

    def get_by_student(self, student):
        if student == PAIRED_STUDENT:
            return PAIR

    def get_by_project(self, project):
        if project == PAIRED_PROJECT:
            return PAIR


class StudentRepositoryStub:

    def get_all_students(self):
        return [UNPAIRED_STUDENT, PAIRED_STUDENT, ANOTHER_UNPAIRED_STUDENT]


class StudentIsMatchedGatewayTest(unittest.TestCase):

    def setUp(self):
        self.gateway = self.create_gateway()

    def test_is_matched_if_pair_with_student_exists(self):
        self.assertTrue(self.gateway.is_matched(PAIRED_STUDENT))

    def test_is_not_matched_if_pair_with_student_does_not_exist(self):
        self.assertFalse(self.gateway.is_matched(UNPAIRED_STUDENT))

    def create_gateway(self):
        return StudentIsMatchedGateway(
            PairRepositoryStub()
        )


class ProjectIsMatchedGatewayTest(unittest.TestCase):

    def setUp(self):
        self.gateway = self.create_gateway()

    def test_is_matched_if_pair_with_project_exists(self):
        self.assertTrue(self.gateway.is_matched(PAIRED_PROJECT))

    def test_is_not_matched_if_pair_with_project_does_not_exist(self):
        self.assertFalse(self.gateway.is_matched(UNPAIRED_PROJECT))

    def create_gateway(self):
        return ProjectIsMatchedGateway(
            PairRepositoryStub()
        )


class StudentIsMatchedGatewayStub:

    def is_matched(self, student):
        if student == PAIRED_STUDENT:
            return True


class UnmatchedStudentsGatewayTest(unittest.TestCase):

    def setUp(self):
        self.gateway = self.create_gateway()

    def test_only_gets_students_which_are_matched(self):
        unmatched_students = self.gateway.get_unmatched_students()

        self.assertListEqual(unmatched_students, UNPAIRED_STUDENTS)

    def create_gateway(self):
        return UnmatchedStudentsGateway(
            StudentRepositoryStub(),
            StudentIsMatchedGatewayStub()
        )
