from student_manager import load_students

def total_students():
    return len(load_students())

if __name__ == "__main__":
    print("Total Students:", total_students())
