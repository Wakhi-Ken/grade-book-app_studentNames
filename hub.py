import sys
from creating_student_rec import creating_student_rec
from course_records import creating_course
from enrolling_student import enrolling_student
# from calculate_ranking import calculate_ranking
# from search_by_grade import search_by_grade
# from generate_transcript import generate_transcript
# from exiting import exiting


def exit_app():
    print("Thanks for using the Grade Book Application")
    print("Goodbye!")
    sys.exit()


def main():
    while True:
        print("\nWelcome to the Grade Book Application")
        print("Please select an option:")
        print("1. Add Student")
        print("2. Add course")
        print("3. Register Student for course")
        print("4. Calculate Ranking")
        print("5. Searching by Grade")
        print("6. Generate Transcript")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            creating_student_rec()
        elif choice == "2":
            creating_course()
        elif choice == "3":
            enrolling_student()
        elif choice == "4":
            calculate_ranking()
        elif choice == "5":
            search_by_grade()
        elif choice == "6":
            generate_transcript()
        elif choice == "7":
            print("Exiting program.")
            break
            exiting()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
