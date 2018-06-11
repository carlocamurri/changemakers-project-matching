class Student:

    def __init__(self, id_number, project_priorities, grade=5, keywords=[], department=''):
        self.id_number = id_number
        self.project_priorities = project_priorities
        if grade > 10 or grade < 0:
            raise ValueError('Student grade not in specified range')
        self.grade = grade
        self.keywords = keywords
        self.department = department
        self.project = None

    @property
    def is_matched(self):
        return self.project is not None
