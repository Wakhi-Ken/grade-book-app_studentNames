def search_by_grade(students):
    min_grade = float(input("Enter minimum GPA: "))
    max_grade = float(input("Enter maximum GPA: "))
    filtered_students = [s for s in students if min_grade <= s.gpa <= max_grade]
    print("Students in the specified GPA range:")
    for student in filtered_students:
        student.calculate_gpa()
        print(f"{student.email} - {student.gpa:.2f}")