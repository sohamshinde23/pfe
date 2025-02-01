#
import os

# File to store student data
data_file = 'students.txt'

# Function to add a student
def add_student(student_id, name, age, grade):
    with open(data_file, 'a') as file:
        file.write(f"{student_id},{name},{age},{grade}\n")
    print(f"Student {name} added successfully!")

# Function to update student info
def update_student(student_id, name=None, age=None, grade=None):
    updated = False
    with open(data_file, 'r') as file:
        students = file.readlines()
    with open(data_file, 'w') as file:
        for student in students:
            data = student.strip().split(',')
            if data[0] == student_id:
                data[1] = name if name else data[1]
                data[2] = age if age else data[2]
                data[3] = grade if grade else data[3]
                updated = True
            file.write(','.join(data) + "\n")
    if updated:
        print(f"Student {student_id} updated successfully!")
    else:
        print(f"Student {student_id} not found!")

# Function to delete a student
def delete_student(student_id):
    deleted = False
    with open(data_file, 'r') as file:
        students = file.readlines()
    with open(data_file, 'w') as file:
        for student in students:
            if student.split(',')[0] != student_id:
                file.write(student)
            else:
                deleted = True
    if deleted:
        print(f"Student {student_id} deleted successfully!")
    else:
        print(f"Student {student_id} not found!")

# Function to view all students
def view_students():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            students = file.read()
        print("Student Records:\n" + students)
    else:
        print("No records found.")

# Main function for user interaction
def main():
    while True:
        print("\n1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            add_student(student_id, name, age, grade)
        elif choice == '2':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter New Name (leave blank to skip): ") or None
            age = input("Enter New Age (leave blank to skip): ") or None
            grade = input("Enter New Grade (leave blank to skip): ") or None
            update_student(student_id, name, age, grade)
        elif choice == '3':
            student_id = input("Enter Student ID to delete: ")
            delete_student(student_id)
        elif choice == '4':
            view_students()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
