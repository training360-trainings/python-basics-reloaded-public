class Student:
    def __init__(self, name, subjects) -> None:
        self.name = name
        self.subjects = subjects


def student_factory():
    students = []
    file = open('students.txt', 'r')
    students_count = int(file.readline())
    for i in range(students_count):
        name = file.readline().strip()
        subject_count = int(file.readline())
        subjects = []
        for j in range(subject_count):
            subjects.append({
                'name': file.readline().strip(),
                'grades':  file.readline().strip().split(', ')
            })
        students.append(Student(name, subjects))
    return students


s = student_factory()
print(s[0].name)
print(s[0].subjects)
print(s[1].name)
print(s[1].subjects)
