students = []

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    student = {"name": name, "marks": marks}
    students.append(student)
    print("Student added!\n")

def view_students():
    if not students:
        print("No records found.\n")
        return
    
    for i, student in enumerate(students):
        print(f"{i+1}. {student['name']} - {student['marks']}")
    print()

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice\n")
