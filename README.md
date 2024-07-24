# grade-book-app_studentNames
grade-book-app_studentNames

hub.py: This is the main entry point of your application. When you run python hub.py or python3 hub.py from the terminal, this file is executed, and it serves as the hub that connects all the different functionalities of your app.


creating_student_rec.py: This file contains a script that allows you to add student information. When you select option 1 while running hub.py, this script is executed, and you can enter a student's details. The information entered is then saved in a file called student_rec.json.


enrolling_student.py: This file contains the same script as creating_student_rec.py. It also allows you to add student information, and the data is saved in the student_rec.json file.

course_records.py: This file has a script that enables you to add course information. When you run this script, you can enter course details, and the information is saved in a file called course.json.

generate_transcript.py: This file contains a script that generates student transcripts. When you run this script, it extracts the relevant student data from the student_rec.json file and generates a transcript for each student. The generated transcripts are then saved in a file called transcript.json.

search_by_grade.py: This file has a script that allows you to search for students based on their GPA (Grade Point Average). The script extracts the student GPA data from the student_rec.json file and then allows you to search for students based on their GPA.

calculate_ranking.py: This file contains a script that calculates the ranking of students. The script sorts the students based on their GPA, from the highest to the lowest, and then assigns a ranking to each student. The ranking information is then saved in the student_rec.json file.
