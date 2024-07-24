# File paths
student_path = './students.txt' 
course_path = './course.txt'
trans_file_path = './Transcript.txt'


with open(student_path, 'r') as student, open(course_path, 'r') as course:
    lines_student = student.readlines()
    lines_course = course.readlines()

with open(trans_file_path, 'w') as trans_file:
    for student, course in zip(lines_student, lines_course):
        trans_file.write(student.strip() + ' ')
        trans_file.write(course.strip() + '\n')

print("Transcript has been successfully made.")
print(trans_file_path)