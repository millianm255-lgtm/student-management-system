from student_manager import load_students

def test_load_students():
    students = load_students()
    assert isinstance(students, list)
