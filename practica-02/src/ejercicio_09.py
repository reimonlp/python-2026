students = [
    {"name": "  Ana García ", "grade": "8", "status": "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status": "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez  ", "grade": None, "status": "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
    {"name": "  ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
    {"name": "  sofía torres ", "grade": "8", "status": "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
    {"name": "roberto díaz", "grade": "", "status": "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
    {"name": "  laura méndez", "grade": "8", "status": "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
]

def clean_student_data(students):
    """Limpia los datos de los estudiantes eliminando registros con datos
    faltantes o inválidos, normalizando los nombres y estados, eliminando
    duplicados por nombre (manteniendo la nota más alta) y ordenando
    alfabéticamente por nombre.
    """

    cleaned_students = []
    seen_names = set()
    students_by_name = {}

    for student in students:
        name = student["name"].strip().title() if student["name"] and student["name"].strip() else None
        grade = student["grade"] if student["grade"] and student["grade"].isdigit() else None
        status = student["status"].strip().title() if student["status"] and student["status"].strip() else None

        if not name or not grade:
            continue

        # Eliminar duplicados por nombre, quedándose con la nota más alta
        if name in students_by_name:
            existing_student = students_by_name[name]
            existing_student["grade"] = max(existing_student["grade"], int(grade))
        else:
            new_student = {"name": name, "grade": int(grade), "status": status}
            cleaned_students.append(new_student)
            seen_names.add(name)
            students_by_name[name] = new_student

    # Ordenar alfabéticamente por nombre
    cleaned_students.sort(key=lambda x: x["name"])

    return cleaned_students

def print_cleaned_students(students):
    """Limpia los datos de los estudiantes y muestra la lista de estudiantes únicos con sus calificaciones y estados."""

    cleaned_students = clean_student_data(students)

    print("Registros limpios de alumnos:")
    print("Nombre                 Nota   Estado")
    print("-" * 42)

    for student in cleaned_students:
        print(f"{student['name']:<22} {student['grade']:<6} {student['status']}")

    print(f"\nTotal de alumnos válidos: {len(cleaned_students)}")

if __name__ == "__main__":
    print_cleaned_students(students)