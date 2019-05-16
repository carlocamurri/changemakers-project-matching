import unittest


SOMETHING = 'Something'


class StudentMockTest(unittest.TestCase):

    def setUp(self):
        self.student_mock = self.create_student_mock()

    def test_is_unmatched_if_match_with_was_not_called(self):
        self.assertFalse(self.student_mock.was_matched_with(SOMETHING))

    def test_no_interactions_if_nothing_was_called(self):
        self.assertTrue(self.student_mock.no_interactions)

    def test_was_matched_if_was_called_correctly(self):
        self.student_mock.match_with(SOMETHING)
        self.assertTrue(self.student_mock.was_matched_with(SOMETHING))

    def test_there_were_interactions_if_was_matched(self):
        self.student_mock.match_with(SOMETHING)
        self.assertFalse(self.student_mock.no_interactions)

    def test_is_matched_if_match_was_called(self):
        self.student_mock.match_with(SOMETHING)
        self.assertTrue(self.student_mock.is_matched)

    def test_was_unmatched_if_was_called(self):
        self.student_mock.unmatch()
        self.assertTrue(self.student_mock.was_unmatched)

    def test_was_not_unmatched_if_was_not_called(self):
        self.assertFalse(self.student_mock.was_unmatched)

    def test_there_were_interactions_if_was_unmatched(self):
        self.student_mock.unmatch()
        self.assertFalse(self.student_mock.no_interactions)

    def test_is_not_matched_if_was_unmatched(self):
        self.student_mock = self.create_student_mock(is_matched=True)
        self.student_mock.unmatch()
        self.assertFalse(self.student_mock.is_matched)

    def create_student_mock(self, is_matched=False):
        return StudentMock(is_matched)


class StudentMock:

    def __init__(self, is_matched):
        self.is_matched = is_matched
        self.no_interactions = True
        self.matched_with = None
        self.was_unmatched = False

    def match_with(self, project):
        self.no_interactions = False
        self.is_matched = True
        self.matched_with = project

    def unmatch(self):
        self.no_interactions = False
        self.is_matched = False
        self.was_unmatched = True

    def was_matched_with(self, project):
        return self.matched_with == project


class ProjectMockTest(unittest.TestCase):

    def setUp(self):
        self.project_mock = self.create_project_mock()

    def test_is_unmatched_if_match_with_was_not_called(self):
        self.assertFalse(self.project_mock.was_matched_with(SOMETHING))

    def test_no_interactions_if_nothing_was_called(self):
        self.assertTrue(self.project_mock.no_interactions)

    def test_was_matched_if_was_called_correctly(self):
        self.project_mock.match_with(SOMETHING)
        self.assertTrue(self.project_mock.was_matched_with(SOMETHING))

    def test_is_matched_if_match_was_called(self):
        self.project_mock.match_with(SOMETHING)
        self.assertTrue(self.project_mock.is_matched)

    def test_there_were_interactions_if_was_matched(self):
        self.project_mock.match_with(SOMETHING)
        self.assertFalse(self.project_mock.no_interactions)

    def test_was_not_unmatched_before_matched_if_nothing_was_called(self):
        self.assertFalse(self.project_mock.was_unmatched_before_being_matched)

    def test_was_unmatched_before_matched_if_only_unmatch_was_called(self):
        self.project_mock.unmatch()
        self.assertTrue(self.project_mock.was_unmatched_before_being_matched)

    def test_was_unmatched_before_matched_if_unmatch_was_called_before_match(self):
        self.project_mock.unmatch()
        self.project_mock.match_with(SOMETHING)
        self.assertTrue(self.project_mock.was_unmatched_before_being_matched)

    def test_was_not_unmatched_before_matched_if_unmatch_was_called_after_match(self):
        self.project_mock.match_with(SOMETHING)
        self.project_mock.unmatch()
        self.assertFalse(self.project_mock.was_unmatched_before_being_matched)

    def test_there_were_interactions_if_was_unmatched(self):
        self.project_mock.unmatch()
        self.assertFalse(self.project_mock.no_interactions)

    def test_is_not_matched_if_was_unmatched(self):
        self.project_mock = self.create_project_mock(is_matched=True)
        self.project_mock.unmatch()
        self.assertFalse(self.project_mock.is_matched)

    def create_project_mock(self, is_matched=False):
        return ProjectMock(
            is_matched,
            student=None
        )


class ProjectMock:

    def __init__(self, is_matched, student):
        self.is_matched = is_matched
        self.student = student
        self.no_interactions = True
        self.matched_with = None
        self.was_unmatched_before_being_matched = False

    def match_with(self, project):
        self.no_interactions = False
        self.is_matched = True
        self.matched_with = project

    def unmatch(self):
        self.no_interactions = False
        self.is_matched = False
        if self.matched_with is None:
            self.was_unmatched_before_being_matched = True

    def was_matched_with(self, project):
        return self.matched_with == project