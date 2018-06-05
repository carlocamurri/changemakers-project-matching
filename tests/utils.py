def create_student(id_number, preferred_projects, grade=10):
    return {
        'id_number': id_number,
        'grade': grade,
        'preferred_projects': preferred_projects
    }
