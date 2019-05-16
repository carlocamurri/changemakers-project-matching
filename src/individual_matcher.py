class IndividualMatcher:

    def __init__(self, priority_calculator):
        self.priority_calculator = priority_calculator

    def match(self, student, project):
        if self.only_project_is_matched(student, project) and \
                self.student_has_higher_priority_than_currently_matched(student, project):
            project.student.unmatch()
            project.unmatch()
        if self.both_unmatched(student, project):
            student.match_with(project)
            project.match_with(student)

    def only_project_is_matched(self, student, project):
        return not student.is_matched and project.is_matched

    def student_has_higher_priority_than_currently_matched(self, student, project):
        return self.priority_calculator(student, project) > self.priority_calculator(project.student, project)

    def both_unmatched(self, student, project):
        return not student.is_matched and not project.is_matched
