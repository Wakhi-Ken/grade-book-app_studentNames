import json

def load_student_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{file_path}'.")
        return []

def search_by_grades(min_gpa, max_gpa, file_path):
    try:
        student_data = load_student_data(file_path)
        found_students = []

        for student in student_data:
            gpa = float(student.get('gpa', 0))  # Use .get() to safely retrieve 'gpa' or default to 0
            if min_gpa <= gpa <= max_gpa:
                found_students.append(student)

        if found_students:
            print(f"Found {len(found_students)} student(s) with GPA between {min_gpa} and {max_gpa}:")
            for student in found_students:
                print(f"Name: {student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}, "
                      f"Email: {student.get('email', 'Unknown')}, GPA: {student.get('gpa', 'Unknown')}")
        else:
            print("No students found with the specified GPA range.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{file_path}'.")

def search_by_grade():
    file_path = './student_rec.json'
    min_gpa = float(input("Enter minimum GPA: "))
    max_gpa = float(input("Enter maximum GPA: "))

    search_by_grades(min_gpa, max_gpa, file_path)

if __name__ == "__main__":
    search_by_grade()
