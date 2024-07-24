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

def load_course_data():
    if os.path.exists('./course.json') and os.path.getsize('./course.json') > 0:
        with open('./course.json', 'r') as file:
            return json.load(file)
    else:
        return []

def save_student(student_data):
    with open('./student_rec.json', 'w') as file:
        json.dump(student_data, file, indent=4)

def save_course(course_data):
    with open('./course.json', 'w') as file:
        json.dump(course_data, file, indent=4)

def creating_student_rec():
    print("Please enter student information:")
    name = input("Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    Course_name = input("Course Name: ")
    Credit_score = input("Credit Score: ")
    Gpa  = input("Gpa: ")

    # Load course data from course.json
    course_data = load_course_data()

    # Check if the course already exists in course.json
    existing_course = next((course for course in course_data if course['name'] == Course_name), None)
    if existing_course:
        # If the course exists, use the existing credit score
        Credit_score = existing_course['credit_score']
    else:
        # If the course doesn't exist, add it to course.json
        new_course = {
            "name": Course_name,
            "credit_score": Credit_score
        }
        course_data.append(new_course)
        save_course(course_data)

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