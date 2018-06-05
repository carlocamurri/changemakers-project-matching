class Project:

    def __init__(self, id_number, professor, project_type, keywords):
        self.id_number = id_number
        self.supervisor = supervisor
        self.project_type = project_type
        self.keywords = keywords
        self.student = None

    def __str__(self):
        return 'Project {}\n'.format(self.id_number) + \
                '\tProfessor: {}\n'.format(self.professor) + \
                '\tProject Type: {}\n'.format(self.project_type) + \
                '\tAssociated Keywords: {}\n'.format(self.project_type) + \
                '\tCurrently Matched Student: {}\n'.format(self.student)
