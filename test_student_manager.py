from student_manager import add_student

def test_add_student():
    students = add_student("John Doe", "SE001", "Software Engineering")
    assert students[-1]["reg_no"] == "SE001"
