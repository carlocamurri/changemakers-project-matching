class Project:

    def __init__(self, id_number, keywords=[], department='', supervisor=None):
        self.id_number = id_number
        self.keywords = keywords
        self.department = department
        self.supervisor = supervisor
        self.student = None

    @property
    def is_matched(self):
        return self.student is not None

    @property
    def priority_split(self):
        return self.supervisor.priority_split
