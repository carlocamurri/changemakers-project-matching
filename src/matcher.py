class Matcher: 

    def __init__(self, students):
        self.students = students

    def match(self):
        while not self.is_stable():
            for student in self.get_unmatched_students():
                for project in student.project_priorities:
                    if not project.is_matched():
                        student.pair(project)
                        break
                    else:
                        if project.student.grade < student.grade:
                            project.student.unpair()
                            student.pair(project)

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

    def get_unmatched_students(self):
        return [student for student in self.students if not student.is_matched()]
