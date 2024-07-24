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

def calculate_gpa(credit_score):
    
    total_credits = sum(credit_score)
    if total_credits == 0:
        return 0.0
    total_score = sum(score * credit for score, credit in credit_score)
    gpa = total_score / total_credits
    return round(gpa, 2)

def generate_transcript(student_data):
    if not student_data:
        print("No student records found.")
        return

    for student in student_data:
        name = f"{student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}"
        email = student.get('email', 'Unknown')
        course_name = student.get('course_name', 'Unknown')
        credit_score = float(student.get('credit_score', 0))
        gpa = float(student.get('gpa', 0))

        
        transcript = f"Transcript for {name} ({email}):\n"
        transcript += f"Course Name: {course_name}\n"
        transcript += f"Credit Score: {credit_score}\n"
        transcript += f"GPA: {gpa}\n"

        print(transcript)
        print()

def main():
    file_path = './student_rec.json'
    student_data = load_student_data(file_path)

    if student_data:
        generate_transcript(student_data)

if __name__ == "__main__":
    main()
