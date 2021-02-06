students = {
    'Henry': 42,
    'Ani': 96,
    'Anna': 84,
    'Narek': 56,
    'Artur': 95
}

new_students = []
for student in students:
    if students[student] < 60:
        new_students.append(student)

for i in new_students:
    students.pop(i)

print(students)
