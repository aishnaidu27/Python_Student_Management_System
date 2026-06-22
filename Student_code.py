student_details=[
    {"ID":1,"Name":"AAA","Course":"BCA","CGPA":9.8},
    {"ID": 2, "Name": "BBB", "Course": "BSC", "CGPA": 6.8},
    {"ID": 3, "Name": "CCC", "Course": "BCA", "CGPA":7.8},
    {"ID": 4, "Name": "DDD", "Course": "BCOM", "CGPA": 7.3},
    {"ID": 5, "Name": "EEE", "Course": "BCOM", "CGPA": 8.8},
    {"ID": 6, "Name": "FFF", "Course": "BSC", "CGPA": 9.4},
    {"ID": 7, "Name": "GGG", "Course": "BSC", "CGPA": 6.4},
]

def view_students():
    for student in student_details:
        print("----------------")
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Course:", student["Course"])
        print("CGPA:", student["CGPA"])

def add_student():
    student_id = int(input("Enter Student ID: "))
    student_name = input("Enter Student Name: ")
    student_course = input("Enter Course: ")
    student_cgpa = float(input("Enter CGPA: "))
    new_student = {
        "ID": student_id,
        "Name": student_name,
        "Course": student_course,
        "CGPA": student_cgpa
    }
    student_details.append(new_student)
    print("----------------")
    print("ID:", new_student["ID"])
    print("Name:", new_student["Name"])
    print("Course:", new_student["Course"])
    print("CGPA:", new_student["CGPA"])
    print("Data added successfully!!")

def search_student():
    search_id = int(input("Enter the ID number to fetch the data of the student:"))
    for student in student_details:
        if student["ID"] == search_id:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Course:", student["Course"])
            print("CGPA:", student["CGPA"])

def delete_student():
    delete_id = int(input("Enter the ID number to remove the data of the student:"))
    for student in student_details:
        if student["ID"] == delete_id:
            student_details.remove(student)
            print("Student deleted successfully!!")
            break
    print("----------------")
    print("ID:", student["ID"])
    print("Name:", student["Name"])
    print("Course:", student["Course"])
    print("CGPA:", student["CGPA"])

while True:
        print("1. View Students")
        print("2. Add Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
           view_students()
        elif choice == 2:
             add_student()
        elif choice == 3:
             search_student()
        elif choice == 4:
             delete_student()
        elif choice == 5:
             break








