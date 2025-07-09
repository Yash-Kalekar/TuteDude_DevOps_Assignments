students = {}

while True:
    print("\nOptions:")
    print("1. Add a new student")
    print("2. Update student grade")
    print("3. Print all students and grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added successfully.")
    
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print("Student not found.")
    
    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    
    elif choice == "4":
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")
