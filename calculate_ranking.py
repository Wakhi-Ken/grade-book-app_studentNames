def calculate_ranking(students):
    students.sort(key=lambda x: x.gpa, reverse=True)
    print("Student Ranking:")
    for i, student in enumerate(students, start=1):
        student.calculate_gpa()
        print(f"{i}. {student.email} - {student.gpa:.2f}")