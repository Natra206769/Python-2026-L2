import curses

from input import input_students, input_courses, input_marks
from output import (
    list_students,
    list_courses,
    list_marks,
    average_gpa
)


students = []
courses = []
marks = {}


def main(stdscr):

    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "STUDENT MANAGEMENT")

        stdscr.addstr(2, 0, "1. Input students")
        stdscr.addstr(3, 0, "2. Input courses")
        stdscr.addstr(4, 0, "3. Input marks")

        stdscr.addstr(5, 0, "4. List students")
        stdscr.addstr(6, 0, "5. List courses")
        stdscr.addstr(7, 0, "6. List marks")
        stdscr.addstr(8, 0, "7. GPA ranking")

        stdscr.addstr(9, 0, "0. Exit")

        stdscr.addstr(11, 0, "Enter your choice: ")
        stdscr.refresh()

        choice = stdscr.getch()

        if choice == ord("1"):
            input_students(stdscr, students)

        elif choice == ord("2"):
            input_courses(stdscr, courses)

        elif choice == ord("3"):
            input_marks(
                stdscr,
                students,
                courses,
                marks
            )

        elif choice == ord("4"):
            list_students(stdscr, students)

        elif choice == ord("5"):
            list_courses(stdscr, courses)

        elif choice == ord("6"):
            list_marks(
                stdscr,
                students,
                courses,
                marks
            )

        elif choice == ord("7"):
            average_gpa(
                stdscr,
                students,
                courses,
                marks
            )

        elif choice == ord("0"):
            break


if __name__ == "__main__":
    curses.wrapper(main)