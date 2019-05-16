import unittest

from src.project import Project
from src.student import Student
from src.priority import grade_priority_calculator
from src.priority import keywords_priority_calculator
from src.priority import department_priority_calculator
from src.priority import split_priority_calculator
from src.priority import PrioritySplit


class GradePriorityCalculatorTest(unittest.TestCase):

    def test_priority_of_student_is_his_grade_normalized(self):
        student = Student(1, ['a_project'], grade=7)
        self.assertEqual(grade_priority_calculator(student), student.grade / 10)


class KeywordsPriorityCalculatorTest(unittest.TestCase):

    def test_priority_of_student_is_one_if_all_keywords_match(self):
        kw_1 = 'kw_1'
        kw_2 = 'kw_2'
        kw_3 = 'kw_3'
        kws = [kw_1, kw_2, kw_3]
        project = Project(1, keywords=kws)
        student = Student(1, [project], keywords=kws)
        self.assertEqual(keywords_priority_calculator(student, project), 1)

    def test_priority_of_student_is_zero_if_none_match(self):
        kw_1 = 'kw_1'
        kw_2 = 'kw_2'
        kw_3 = 'kw_3'
        kw_4 = 'kw_4'
        student_kws = [kw_1, kw_2]
        project_kws = [kw_3, kw_4]
        project = Project(1, keywords=project_kws)
        student = Student(1, [project], keywords=student_kws)
        self.assertEqual(keywords_priority_calculator(student, project), 0)

    def test_priority_of_student_is_one_if_all_project_keywords_match(self):
        kw_1 = 'kw_1'
        kw_2 = 'kw_2'
        kw_3 = 'kw_3'
        student_kws = [kw_1, kw_2, kw_3]
        project_kws = [kw_1]
        project = Project(1, keywords=project_kws)
        student = Student(1, [project], keywords=student_kws)
        self.assertEqual(keywords_priority_calculator(student, project), 1)

    def test_priority_of_student_is_ratio_of_project_keywords_matched(self):
        project_kws = self.n_keywords(10)
        student_kws = self.n_keywords(2)
        student_kws += self.other_keywords(37)
        project = Project(1, keywords=project_kws)
        student = Student(1, [project], keywords=student_kws)
        self.assertEqual(keywords_priority_calculator(student, project), 0.2)

    def n_keywords(self, n):
        return ['kw_{}'.format(i) for i in range(1, n + 1)]

    def other_keywords(self, n):
        return ['other' for _ in range(n)]


class DepartmentPriorityCalculatorTest(unittest.TestCase):

    def test_priority_should_be_zero_if_department_does_not_match(self):
        dept_1 = 'dept_1'
        dept_2 = 'dept_2'
        project = Project(1, department=dept_1)
        student = Student(1, [project], department=dept_2)
        self.assertEqual(department_priority_calculator(student, project), 0)

    def test_priority_should_be_one_if_departments_match(self):
        dept = 'dept'
        project = Project(1, department=dept)
        student = Student(1, [project], department=dept)
        self.assertEqual(department_priority_calculator(student, project), 1)


class SplitPriorityCalculatorTest(unittest.TestCase):

    def test_split_calculator_is_weighted_correctly(self):
        grade_score = 0.7
        keywords_score = 0.2
        department_score = 1
        def grade_calculator(student, project):
            return grade_score
        def keywords_calculator(student, project):
            return keywords_score
        def department_calculator(student, project):
            return department_score
        split = PrioritySplit(0.5, 0.3, 0.2)
        project = ProjectStub(split)
        self.assertEqual(split_priority_calculator(
            'a_student', \
            project, \
            grade_calculator=grade_calculator, \
            keywords_calculator=keywords_calculator, \
            department_calculator=department_calculator \
        ), 0.35 + 0.06 + 0.2)


class ProjectStub:

    def __init__(self, priority_split):
        self.priority_split = priority_split


class PrioritySplitTest(unittest.TestCase):

    def test_priority_split_is_normalized(self):
        original_grade_weight = 0.5
        original_keywords_weight = 0.3
        original_department_weight = 0.2
        multiplier = 32
        new_grade_weight = 0.5 * multiplier
        new_keywords_weight = 0.3 * multiplier
        new_department_weight = 0.2 * multiplier
        priority_split = PrioritySplit( \
            grade_weight=new_grade_weight, \
            keywords_weight=new_keywords_weight, \
            department_weight=new_department_weight \
        )
        self.assertEqual(priority_split.grade_weight, original_grade_weight)
        self.assertEqual(priority_split.keywords_weight, original_keywords_weight)
        self.assertEqual(priority_split.department_weight, original_department_weight)

    def test_error_raised_on_negative_grade_weight(self):
        self.assertRaises(
            ValueError, \
            PrioritySplit, \
            grade_weight=-1, \
            keywords_weight=2, \
            department_weight=3 \
        )

    def test_error_raised_on_negative_keyword_weight(self):
        self.assertRaises(
            ValueError, \
            PrioritySplit, \
            grade_weight=1, \
            keywords_weight=-2, \
            department_weight=3 \
        )

    def test_error_raised_on_negative_department_weight(self):
        self.assertRaises(
            ValueError, \
            PrioritySplit, \
            grade_weight=1, \
            keywords_weight=2, \
            department_weight=-4 \
        )
