class Matcher:

    def __init__(self, students):
        self.students = students

    def match(self):
        for student in self.students:
            student.project = student.project_priorities[0]

    def is_stable(self):
        for student in self.students:
            if not student.is_matched():
                return False
        return True

    def get_available_projects(self):
        available_projects = set(self.students[0].project_priorities)
        for student in self.students:
            if student.is_matched():
                available_projects.remove(student.project)
        return available_projects
