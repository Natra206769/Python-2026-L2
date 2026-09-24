students = []
courses = []
marks = {}

#input student, course, mark
def input_students():
    numStudents = int(input("Number of students: "))

    for i in range(numStudents):
        print(f"Student {i + 1}")
        studentId = int(input("Student ID: "))
        name = input("Name of student: ")
        doB = input("Date of birth: ")

        student = {
            "id": studentId,
            "name": name,
            "doB": doB 
        }

        students.append(student)


def input_courses():
    numCourses = int(input("Number of courses: "))

    for i in range(numCourses):
        print(f"Course {i + 1}: ")
        name = input("Name of course: ")
        courseId = input("ID course: ")

        course = {
            "name": name,
            "id": courseId
        }

        courses.append(course)
    

def input_marks():
    list_courses()
    course_id = input("Enter the course: ")
    marks[course_id] = {}

    for student in students:
        mark = float(input(f"Enter the mark of {student["name"]}: "))
        marks[course_id][student["id"]] = mark


#list student, course, mark
def list_students():
    for student in students:
        print(student["id"], student["name"], student["doB"])


def list_courses():
    for course in courses:
        print(course["id"], course["name"])

def list_marks():
    list_courses()
    course_id = input("Enter the ID course: ")

    if course_id not in marks:
        print("Not mark available")

    for student in students:
        print(student["name"], marks[course_id][student["id"]])
