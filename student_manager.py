import json

DATA_FILE = "students.json"

def load_students():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

def add_student(name, reg_no, course):
    students = load_students()
    students.append({
        "name": name,
        "reg_no": reg_no,
        "course": course
    })
    save_students(students)
    return students
