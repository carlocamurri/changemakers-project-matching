class StudentPool:

    def __init__(self, students):
        self.students = students

    def get_unmatched(self):
        return [student for student in self.students if not student.project]

    def __str__(self):
        string = 'Student Pool:\n---------------------\n'
        for student in self.students:
            string += str(student)
            string += '\n'
        return string

