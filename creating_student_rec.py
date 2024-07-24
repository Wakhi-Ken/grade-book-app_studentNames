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

def student_records():
    if os.path.exists('records.json') and os.path.getsize('records.json') > 0:
        with open('records.json', 'r') as file:
            return json.load(file)
    else:
        default_students = [
            {
                "name": "Prince",
                "last_name": "Doe",
                "email": "prince.doe@gmail.com",
                "course_name": "Introduction to Python",
                "credit_score": "70",
                "gpa": "3.4"
            },
            {
                "name": "Luke",
                "last_name": "Smith",
                "email": "luke.smith@gmail.com",
                "course_name": "Introduction to SQL",
                "credit_score": "80",
                "gpa": "3.9"
            }
        ]
        return default_students

def save_student(student_data):
    with open('records.json', 'w') as file:
        json.dump(student_data, file, indent=4)

def creating_student():
    print("Please enter student information:")
    name = input("Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    course_name = input("Course Name: ")
    credit_score = input("Credit Score: ")
    gpa = input("GPA: ")

    new_student = Student(name, last_name, email, course_name, credit_score, gpa)

    print("\nNew student added successfully:")
    print("Name:", new_student.name, new_student.last_name)
    print("Email:", new_student.email)
    print("Course Name:", new_student.course_name)
    print("Credit Score:", new_student.credit_score)
    print("GPA:", new_student.gpa)

    existing_data = student_records()

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