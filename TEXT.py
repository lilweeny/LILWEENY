from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    major: str
    gpa: float

    def display_info(self):
      print(f'Имя: {student.name}, возраст: {student.age}, специальность: {student.major}, средний балл: {student.gpa}.')

    def calculate_grade(self):
        if student.gpa <= 2.7:
            return 'Неудовлетворительно'
        if 2.7 < student.gpa <= 3.7:
            return 'Удовлетворительно'
        if 3.7 < student.gpa <= 4.7:
            return 'Хорошо'
        if 4.7 < student.gpa <= 5:
            return 'Отлично'

def sort_gpa(students):
    return sorted(students, key=lambda student: student.gpa, reverse=True)

students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9),
    Student("Eve", 19, "Biology", 3.9)
]

for student in students:
    student.display_info()

print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])
print("Are Eve and Eve the same student?", students[4] == students[5])

for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")

sorted_students = sort_gpa(students)
for student in sorted_students:
    student.display_info()