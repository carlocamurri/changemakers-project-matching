from src.priority import grade_priority_calculator


class Matcher:

    def __init__(self, students, priority_calculator=grade_priority_calculator):
        self.students = students
        self.priority_calculator = priority_calculator

    def match(self):
        while not self.is_stable():
            for student in self.get_unmatched_students():
                for project in student.project_priorities:
                    if not project.is_matched():
                        self.pair(student, project)
                        break
                    else:
                        if self.priority_calculator(project.student, project) \
                                < self.priority_calculator(student, project):
                            project.student.project = None
                            self.pair(student, project)
                            break

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

    def pair(self, student, project):
        student.project = project
        project.student = student
