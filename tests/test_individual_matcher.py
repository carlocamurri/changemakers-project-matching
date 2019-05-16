import unittest

from tests.test_doubles import StudentMock, ProjectMock

from src.individual_matcher import IndividualMatcher


class IndividualMatcherTest(unittest.TestCase):

    def test_matches_student_with_project_if_project_and_student_are_not_matched(self):
        matcher = self.create_matcher()
        student = self.student_mock(is_matched=False)
        project = self.project_mock(is_matched=False)

        matcher.match(student, project)

        self.assert_were_reciprocally_matched(student, project)

    def test_nothing_happens_if_student_is_already_matched(self):
        matcher = self.create_matcher()
        student = self.student_mock(is_matched=True)
        project = self.project_mock(is_matched=False)

        matcher.match(student, project)

        self.assert_no_interactions_between(student, project)

    def test_nothing_happens_if_project_is_already_matched_with_student_with_higher_priority(self):
        lower_priority_student = self.student_mock(is_matched=False)
        prioritized_student = self.student_mock(is_matched=True)
        project = self.project_mock(is_matched=True, matched_with=prioritized_student)
        matcher = self.create_matcher_prioritizing_student(prioritized_student)

        matcher.match(lower_priority_student, project)

        self.assert_no_interactions_between(
            lower_priority_student,
            prioritized_student,
            project
        )

    def test_lower_priority_student_gets_unmatched_if_project_is_matched_with_her(self):
        prioritized_student = self.student_mock(is_matched=False)
        lower_priority_student = self.student_mock(is_matched=True)
        project = self.project_mock(is_matched=True, matched_with=lower_priority_student)

        matcher = self.create_matcher_prioritizing_student(prioritized_student)

        matcher.match(prioritized_student, project)

        self.assertTrue(lower_priority_student.was_unmatched)

    def test_project_gets_matched_with_higher_priority_student_if_is_matched_with_lower_priority_one(self):
        prioritized_student = self.student_mock(is_matched=False)
        lower_priority_student = self.student_mock(is_matched=True)
        project = self.project_mock(is_matched=True, matched_with=lower_priority_student)

        matcher = self.create_matcher_prioritizing_student(prioritized_student)

        matcher.match(prioritized_student, project)

        self.assert_unmatches_and_matches_with(project, prioritized_student)

    def test_higher_priority_student_gets_matched_with_project_if_project_is_matched_with_lower_priority_one(self):
        prioritized_student = self.student_mock(is_matched=False)
        lower_priority_student = self.student_mock(is_matched=True)
        project = self.project_mock(is_matched=True, matched_with=lower_priority_student)

        matcher = self.create_matcher_prioritizing_student(prioritized_student)

        matcher.match(prioritized_student, project)

        self.assertTrue(prioritized_student.was_matched_with(project))

    def assert_were_reciprocally_matched(self, student, project):
        self.assertTrue(student.was_matched_with(project))
        self.assertTrue(project.was_matched_with(student))

    def assert_no_interactions_between(self, *interactables):
        for interactable in interactables:
            self.assertTrue(interactable.no_interactions)

    def assert_unmatches_and_matches_with(self, project, student):
        self.assertTrue(project.was_unmatched_before_being_matched)
        self.assertTrue(project.was_matched_with(student))

    def student_mock(self, is_matched):
        return StudentMock(is_matched)

    def project_mock(self, is_matched, matched_with=None):
        return ProjectMock(is_matched, student=matched_with)

    def create_matcher(self, priority_calculator=None):
        return IndividualMatcher(priority_calculator)

    def create_matcher_prioritizing_student(self, student_to_prioritize):
        def priority_calculator_stub(student, project):
            if student == student_to_prioritize:
                return 0.9
            else:
                return 0.5
        return self.create_matcher(priority_calculator=priority_calculator_stub)


