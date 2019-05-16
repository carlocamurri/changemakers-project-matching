class StudentIsMatchedGateway:

    def __init__(self, pair_repository):
        self.pair_repository = pair_repository

    def is_matched(self, student):
        return self.pair_repository.get_by_student(student) is not None


class ProjectIsMatchedGateway:

    def __init__(self, pair_repository):
        self.pair_repository = pair_repository

    def is_matched(self, project):
        return self.pair_repository.get_by_project(project) is not None


class UnmatchedStudentsGateway:

    def __init__(self, student_repository, student_is_matched_gateway):
        self.student_repository = student_repository
        self.student_is_matched_gateway = student_is_matched_gateway

    def get_unmatched_students(self):
        all_students = self.student_repository.get_all_students()
        return list(filter(
            lambda student: not self.student_is_matched_gateway.is_matched(student),
            all_students
        ))
