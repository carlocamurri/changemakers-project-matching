def match(students):
    for student in students:
        student.project = student.project_priorities[0]

def is_stable(students):
    for student in students:
        if not student.is_matched():
            return False
    return True

def get_available_projects(students):
    available_projects = set(students[0].project_priorities)
    for student in students:
        if student.is_matched():
            available_projects.remove(student.project)
    return available_projects
