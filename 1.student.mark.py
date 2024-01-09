def input_student_info():
    num_students = int(input("Enter number of students: "))
    if num_students == 0:
        print("No students to input. Exiting...")
        return None
    students = []
    for i in range(num_students):
        student_id = input(f"Enter ID for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        dob = input(f"Enter Date of Birth for student {i+1} (MM/DD/YYYY): ")
        students.append({'id': student_id, 'name': name, 'dob': dob})
    return students

def input_course_info():
    num_courses = int(input("Enter number of courses: "))
    courses = []
    for i in range(num_courses):
        course_id = input(f"Enter ID for course {i+1}: ")
        name = input(f"Enter name for course {i+1}: ")
        courses.append({'id': course_id, 'name': name})
    return courses

def input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    for course in courses:
        if course['id'] == course_id:
            for student in students:
                marks = float(input(f"Enter marks for {student['name']} in {course['name']}: "))
                student.setdefault('courses', {}).setdefault(course_id, []).append(marks)

def main():
    student_info = input_student_info()
    if student_info is not None:
        course_info = input_course_info()
        input_marks(student_info, course_info)
        print("Marks entered successfully!")
        student_id = input("Enter student ID to check grade: ")
        course_id = input("Enter course ID to check grade: ")
        get_student_grade(student_info, student_id, course_id)
        
def get_student_grade(students, student_id, course_id):
    for student in students:
        if student['id'] == student_id:
            marks = student.get('courses', {}).get(course_id)
            if marks:
                grade = calculate_grade(sum(marks) / len(marks))
                print(f"Grade for {student['name']} in course {course_id} is {grade}")
                break
            else:
                print(f"No marks found for {student['name']} in course {course_id}")
                break
    else:
        print(f"Student with ID {student_id} not found")

if __name__ == "__main__":
    main()
