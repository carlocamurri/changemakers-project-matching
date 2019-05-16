class Pair:

    def __init__(self, student, project):
        self.student = student
        self.project = project


class PairFactory:

    def create(self, student, project):
        return Pair(student, project)