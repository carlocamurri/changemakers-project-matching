import unittest

from src.commands import MatchPair, MatchPairRequestModel, UnmatchPairByProject, UnmatchPairByProjectRequestModel

STUDENT = 'An Unmatched Student'
PROJECT = 'An Unmatched Project'
PAIR = 'A Pair'


class PairRepositoryMock:

    def __init__(self):
        self.was_added_correctly = False
        self.was_removed_by_project_correctly = False

    def add(self, pair):
        if pair == PAIR:
            self.was_added_correctly = True

    def remove_by_project(self, project):
        if project == PROJECT:
            self.was_removed_by_project_correctly = True


class PairFactoryMock:

    def __init__(self):
        self.was_called_correctly = False

    def create(self, student, project):
        if student == STUDENT and project == PROJECT:
            self.was_called_correctly = True
        return PAIR


class MatchPairTest(unittest.TestCase):

    def setUp(self):
        self.factory_mock = PairFactoryMock()
        self.repository_mock = PairRepositoryMock()
        self.match_pair = self.create_match_pair(STUDENT, PROJECT)

    def test_pair_factory_is_called_correctly(self):
        self.match_pair.execute()

        self.assertTrue(self.factory_mock.was_called_correctly)

    def test_created_pair_is_stored_in_repository(self):
        self.match_pair.execute()

        self.assertTrue(self.repository_mock.was_added_correctly)

    def create_match_pair(self, student, project):
        return MatchPair(
            MatchPairRequestModel(student, project),
            self.factory_mock,
            self.repository_mock
        )


class UnmatchPairByProjectTest(unittest.TestCase):

    def setUp(self):
        self.repository_mock = PairRepositoryMock()
        self.unmatch_pair = self.create_unmatch_pair(PROJECT)

    def test_removes_pair_from_repository_by_project(self):
        self.unmatch_pair.execute()

        self.assertTrue(self.repository_mock.was_removed_by_project_correctly)

    def create_unmatch_pair(self, PROJECT):
        return UnmatchPairByProject(
            UnmatchPairByProjectRequestModel(PROJECT),
            self.repository_mock
        )
