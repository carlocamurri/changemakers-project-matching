class Project:

    def __init__(self, id_number, keywords=[], department=''):
        self.id_number = id_number
        self.keywords = keywords
        self.department = department
        self.student = None

    def is_matched(self):
        return self.student is not None
