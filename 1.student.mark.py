s = int(input("Enter number of students: "))


def addstudent():
    student = {}
    for i in range(s):
        student_id = input("Enter student ID: ")
        student_name = input(f"Enter student name: ")
        student_dob = input(f"Enter student date of birth: ")
        student[student_id] = {'Name': student_name, 'DoB': student_dob}
    return student

student_info = addstudent()


c = int(input("Enter number of courses: "))

def addcourse():
    course = {}
    for i in range(c):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course[course_id] = course_name

    return course
course_info = addcourse()

def inputmarks(student_info, course_info):
    mark = {}

    for course_id in course_info:
        mark[course_id] = {}
        for student_id in student_info:
            m = float(input(f"Enter mark for {student_info[student_id]['Name']} ({student_id}): "))
            mark[course_id][student_id] = m

    return mark

marksheet = inputmarks()

def print_student_info():
    print("Student information: ")
    for student_id in student_info.items():
        print(f"Student ID: {student_id}")
        for key, value in student_info.items():
            print(f"{key}: {value}")
        print("\n")

def print_course_info():
    print("Course information: ")
    for course_id in course_info.items():
        print(f"Course ID: {course_id}")
        for key, value in course_info.items():
            print(f"{key}: {value}")
        print("\n")

def print_marks():
    print("Marks: ")
    for course_id, course_mark in mark.items():
        print("Course ID:", course_id)
    for student_id, mark in course_mark.items():
        print(f"Student ID: {student_id}, Mark: {mark}")
    print("\n")

print_student_info()
print_course_info()
print_marks()