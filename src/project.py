class Project:

    def __init__(self, id_number):
        self.id_number = id_number
        self.student = None

    def is_matched(self):
        return self.student is not None
