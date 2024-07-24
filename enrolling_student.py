class Course_Enrollment:
    def __init__(self, name, last_name, email, course_name):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.course_name = course_name


def enrolling_student():
    print("Please enter student information:")
    name = input("Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    course_name = input("Course Name: ")

    new_enrollment = Course_Enrollment(name, last_name, email, course_name)

    print("\nNew student enrolled successfully:")
    print("Name:", new_enrollment.name, new_enrollment.last_name)
    print("Email:", new_enrollment.email)
    print("Course Name:", new_enrollment.course_name)

if __name__ == "__main__":
    enrolling_student()
