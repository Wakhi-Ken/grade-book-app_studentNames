import json
import os

class Student:
    def __init__(self, name, last_name, email, course_name=None, credit_score=None, gpa=None):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.course_name = course_name
        self.credit_score = credit_score
        self.gpa = gpa

def load_existing_data():
    if os.path.exists('./student_rec.json') and os.path.getsize('./student_rec.json') > 0:
        with open('./student_rec.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save_student(student_data):
    with open('./student_rec.json', 'w') as file:
        json.dump(student_data, file, indent=4)

def creating_student_rec():
    print("Please enter student information:")
    name = input("Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    Course_name = input("Course Name: ")
    Credit_score = input("Credit Score: ")
    Gpa  = input("Gpa: ")


    new_student = Student(name, last_name, email, Course_name, Credit_score, Gpa)

    print("\nNew student added successfully:")
    print("Name:", new_student.name, new_student.last_name)
    print("Email:", new_student.email)
    print("Course Name:", new_student.course_name)
    print("Credit Score:", new_student.credit_score)
    print("GPA:", new_student.gpa)

    existing_data = load_existing_data()

    print(f"Existing data: {existing_data}")

    existing_data.append({
        "name": new_student.name,
        "last_name": new_student.last_name,
        "email": new_student.email,
        "course_name": new_student.course_name,
        "credit_score": new_student.credit_score,
        "gpa": new_student.gpa
    })

    save_student(existing_data)

    print("Student information saved")