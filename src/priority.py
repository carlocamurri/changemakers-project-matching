def grade_priority_calculator(student, project=None):
    return student.grade / 10


def keywords_priority_calculator(student, project):
    ratio = 0
    for kw in student.keywords:
        if kw in project.keywords:
            ratio += 1 / len(project.keywords)
    return ratio


def department_priority_calculator(student, project):
    return 1 if student.department == project.department else 0


class PrioritySplit:

    def __init__(self, grade_weight, keywords_weight, department_weight):
        if grade_weight < 0 or keywords_weight < 0 or department_weight < 0:
            raise ValueError('Illegal Argument: Negative weight')
        total = grade_weight + keywords_weight + department_weight
        self.grade_weight = grade_weight / total
        self.keywords_weight = keywords_weight / total
        self.department_weight = department_weight / total
