class Matcher:

    def __init__(self, students):
        self.students = students

    def match(self):
        while not self.is_stable():
            for student in self.get_unmatched_students():
                for project in student.project_priorities:
                    if not self.project_is_matched(project):
                        student.project = project
                        break
                    else:
                        current_student = self.get_matched_student(project)
                        if current_student.grade < student.grade:
                            current_student.project = None
                            student.project = project

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

    def get_matched_student(self, project_id):
        for student in self.students:
            if student.project == project_id:
                return student
        return None

    def project_is_matched(self, project_id):
        return self.get_matched_student(project_id) is not None

    def get_unmatched_students(self):
        return [student for student in self.students if not student.is_matched()]
