# Grades / Exams Manager

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


students = {}  # key: student name, value: Student object


def add_student(name):
    if name not in students:
        students[name] = Student(name)


def add_grade(name, grade):
    if name in students:
        students[name].add_grade(grade)


def show_students():
    for name, student in students.items():
        print(
            f"Name: {name}, "
            f"Grades: {student.grades}, "
            f"Average: {student.average_grade()}"
        )


# ---- main program ----

add_student("Alice")
add_student("Bob")

add_grade("Alice", 5)
add_grade("Alice", 4)
add_grade("Bob", 3)

show_students()
