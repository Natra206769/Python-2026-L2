import curses
import numpy


def list_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "LIST OF STUDENTS")

    row = 2

    for student in students:
        stdscr.addstr(
            row, 0,
            f"{student.id} - {student.name} - {student.dob}"
        )
        row += 1

    stdscr.addstr(row + 1, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()


def list_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "LIST OF COURSES")

    row = 2

    for course in courses:
        stdscr.addstr(
            row, 0,
            f"{course.id} - {course.name} - {course.credit} credits"
        )
        row += 1

    stdscr.addstr(row + 1, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()


def list_marks(stdscr, students, courses, marks):
    stdscr.clear()

    stdscr.addstr(0, 0, "LIST OF COURSES")

    row = 2

    for course in courses:
        stdscr.addstr(
            row, 0,
            f"{course.id} - {course.name}"
        )
        row += 1

    stdscr.addstr(row + 1, 0, "Enter course ID: ")

    curses.echo()
    course_id = stdscr.getstr(
        row + 1, 17
    ).decode("utf-8")
    curses.noecho()

    stdscr.clear()

    if course_id not in marks:
        stdscr.addstr(0, 0, "No marks available")
        stdscr.getch()
        return

    stdscr.addstr(0, 0, f"MARKS - {course_id}")

    row = 2

    for student in students:
        stdscr.addstr(
            row, 0,
            f"{student.name}: {marks[course_id][student.id]}"
        )
        row += 1

    stdscr.addstr(row + 1, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()


def average_gpa(stdscr, students, courses, marks):
    stdscr.clear()

    gpa_list = []

    for student in students:
        student_marks = []
        student_credits = []

        for course in courses:
            course_id = course.id

            student_marks.append(
                marks[course_id][student.id]
            )

            student_credits.append(
                course.credit
            )

        student_marks = numpy.array(student_marks)
        student_credits = numpy.array(student_credits)

        total_marks = numpy.sum(
            student_marks * student_credits
        )

        total_credits = numpy.sum(student_credits)

        avg_gpa = total_marks / total_credits

        gpa_list.append({
            "name": student.name,
            "gpa": avg_gpa
        })

    # Highest GPA first
    gpa_list.sort(
        key=lambda student: student["gpa"],
        reverse=True
    )

    stdscr.addstr(0, 0, "GPA RANKING")

    row = 2

    for student in gpa_list:
        stdscr.addstr(
            row, 0,
            f"{student['name']}: {student['gpa']:.2f}"
        )
        row += 1

    stdscr.addstr(row + 1, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()