class Student:

    def __init__(self, id_number, project_priorities, grade=5):
        self.id_number = id_number
        self.project_priorities = project_priorities
        self.grade = grade
        self.project = None

    def is_matched(self):
        return self.project is not None