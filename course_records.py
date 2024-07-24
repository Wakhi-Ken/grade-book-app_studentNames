import json
import os

class Course:
    def __init__(self, course_name, trimester, credit_score):
        self.course_name = course_name
        self.trimester = trimester
        self.credit_score = credit_score

def course_records():
    if os.path.exists('course.json') and os.path.getsize('course.json') > 0:
        with open('course.json', 'r') as file:
            return json.load(file)
    else:
        
        default_courses = [
            {
                "Course Name": "Introduction to Linux",
                "Trimester": "January 2023",
                "Credit Score": "100"
            },
            {
                "Course Name": "Introduction to Python",
                "Trimester": "February 2023",
                "Credit Score": "100"
            },
            {
                "Course Name": "Introduction to SQL",
                "Trimester": "March 2023",
                "Credit Score": "100"
            }
        ]
        return default_courses

def save_course(course_data):
    with open('course.json', 'w') as file:
        json.dump(course_data, file, indent=4)

def creating_course():
    print("Please enter course information:")
    course_name = input("Course Name: ")
    trimester = input("Trimester in Month Year format: ")
    credit_score = input("Credit Score: ")

    new_course = Course(course_name, trimester, credit_score)

    print("\nNew Course added successfully:")
    print("Course Name:", new_course.course_name)
    print("Trimester:", new_course.trimester)
    print("Credit Score:", new_course.credit_score)

    existing_data = course_records()

    existing_data.append({
        "Course Name": new_course.course_name,
        "Trimester": new_course.trimester,
        "Credit Score": new_course.credit_score
    })

    save_course(existing_data)

    print("Course information saved to course.json.")
