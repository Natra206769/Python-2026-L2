import curses
import math

from domains.student import Student
from domains.course import Course


def get_input(stdscr, row, text):
    stdscr.addstr(row, 0, text)
    stdscr.refresh()

    curses.echo()
    value = stdscr.getstr(row, len(text)).decode("utf-8")
    curses.noecho()

    return value


def input_students(stdscr, students):
    stdscr.clear()

    numStudents = int(
        get_input(stdscr, 0, "Number of students: ")
    )

    row = 2

    for i in range(numStudents):
        stdscr.addstr(row, 0, f"Student {i + 1}")
        row += 1

        studentId = int(
            get_input(stdscr, row, "Student ID: ")
        )
        row += 1

        name = get_input(stdscr, row, "Name: ")
        row += 1

        dob = get_input(stdscr, row, "Date of birth: ")
        row += 2

        student = Student(studentId, name, dob)
        students.append(student)


def input_courses(stdscr, courses):
    stdscr.clear()

    numCourses = int(
        get_input(stdscr, 0, "Number of courses: ")
    )

    row = 2

    for i in range(numCourses):
        stdscr.addstr(row, 0, f"Course {i + 1}")
        row += 1

        courseId = get_input(stdscr, row, "Course ID: ")
        row += 1

        name = get_input(stdscr, row, "Course name: ")
        row += 1

        credit = int(
            get_input(stdscr, row, "Number of credits: ")
        )
        row += 2

        course = Course(courseId, name, credit)
        courses.append(course)


def input_marks(stdscr, students, courses, marks):
    stdscr.clear()

    row = 0

    for course in courses:
        stdscr.addstr(row, 0, f"{course.id} - {course.name}")
        row += 1

    course_id = get_input(
        stdscr,
        row + 1,
        "Enter course ID: "
    )

    marks[course_id] = {}

    row += 3

    for student in students:
        mark = float(
            get_input(
                stdscr,
                row,
                f"Mark of {student.name}: "
            )
        )

        mark = math.floor(mark * 10) / 10

        marks[course_id][student.id] = mark
        row += 1