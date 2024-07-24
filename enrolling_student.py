import json
import os

class Student:
    def __init__(self, name, last_name, email, course_name=None):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.course_name = course_name

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

def enrolling_student():
    print("Please enter student information:")
    name = input("Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    course_name = input("Course Name: ")

    course_data = load_course_data()

    existing_course = next((course for course in course_data if course['Course Name'] == course_name), None)
    if not existing_course:
        new_course = {
            "name": course_name
        }
        course_data.append(new_course)
        save_course(course_data)

    new_student = Student(name, last_name, email, course_name)

    print("\nNew student added successfully:")
    print("Name:", new_student.name, new_student.last_name)
    print("Email:", new_student.email)
    print("Course Name:", new_student.course_name)

    existing_data = load_existing_data()

    print(f"Existing data: {existing_data}")

    existing_data.append({
        "name": new_student.name,
        "last_name": new_student.last_name,
        "email": new_student.email,
        "course_name": new_student.course_name
    })

    save_student(existing_data)

    print("Student information saved")