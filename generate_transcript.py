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

def generate_transcripts(student_data):
    transcripts = []

    for student in student_data:
        name = f"{student.get('name', 'Unknown')} {student.get('last_name', 'Unknown')}"
        email = student.get('email', 'Unknown')
        course_name = student.get('course_name', 'Unknown')
        credit_score = float(student.get('credit_score', 0))
        gpa = float(student.get('gpa', 0))

        transcript = {
            "name": name,
            "email": email,
            "course_name": course_name,
            "credit_score": credit_score,
            "gpa": gpa
        }
        transcripts.append(transcript)

        # Print the transcript
        print(f"Transcript for {name} ({email}):")
        print(f"Course Name: {course_name}")
        print(f"Credit Score: {credit_score}")
        print(f"GPA: {gpa}")
        print()

    return transcripts

def save_transcripts(transcripts, file_path):
    try:
        with open(file_path, 'r') as file:
            existing_transcripts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_transcripts = []

    all_transcripts = existing_transcripts + transcripts

    with open(file_path, 'w') as file:
        json.dump(all_transcripts, file, indent=4)

def generate_transcript():
    file_path = './student_rec.json'
    student_data = load_student_data(file_path)

    if student_data:
        transcripts = generate_transcripts(student_data)
        save_transcripts(transcripts, './transcript.json')

if __name__ == "__main__":
    generate_transcript()