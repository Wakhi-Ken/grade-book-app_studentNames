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

def sort_students_by_gpa(student_data):
    sorted_students = sorted(student_data, key=lambda x: float(x.get('gpa', 0)), reverse=True)
    return sorted_students

def display_student_ranking(sorted_students):
    if sorted_students:
        print("Student Ranking by GPA (Highest to Lowest):")
        rank = 1
        for student in sorted_students:
            print(f"Rank {rank}: {student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}, "
                  f"Email: {student.get('email', 'Unknown')}, GPA: {student.get('gpa', 'Unknown')}")
            rank += 1
    else:
        print("No student records found.")

def calculate_ranking():
    file_path = './student_rec.json'
    student_data = load_student_data(file_path)

    if student_data:
        sorted_students = sort_students_by_gpa(student_data)
        display_student_ranking(sorted_students)

if __name__ == "__main__":
    calculate_ranking()
