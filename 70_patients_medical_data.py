# To keep record of patients’ medical data, manipulate files to store, update, and delete such info 
import os

FILE_NAME = "patients.txt"

def add_patient(patient_id, name, age, gender, diagnosis, treatment):
    with open(FILE_NAME, "a") as file:
        file.write(f"{patient_id},{name},{age},{gender},{diagnosis},{treatment}\n")
    print(f"Patient {name} added successfully.")

def view_patients():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            patient_id, name, age, gender, diagnosis, treatment = line.strip().split(",")
            print(f"ID: {patient_id}, Name: {name}, Age: {age}, Gender: {gender}, Diagnosis: {diagnosis}, Treatment: {treatment}")

def update_patient(patient_id, new_name=None, new_age=None, new_gender=None, new_diagnosis=None, new_treatment=None):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    updated = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            current_id, name, age, gender, diagnosis, treatment = line.strip().split(",")
            if current_id == patient_id:
                name = new_name if new_name else name
                age = new_age if new_age else age
                gender = new_gender if new_gender else gender
                diagnosis = new_diagnosis if new_diagnosis else diagnosis
                treatment = new_treatment if new_treatment else treatment
                updated = True
                file.write(f"{current_id},{name},{age},{gender},{diagnosis},{treatment}\n")
            else:
                file.write(line)

    if updated:
        print(f"Record for patient ID {patient_id} updated.")
    else:
        print(f"No record found for patient ID {patient_id}.")

def delete_patient(patient_id):
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    deleted = False
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            current_id, _, _, _, _, _ = line.strip().split(",")
            if current_id == patient_id:
                deleted = True
                continue
            file.write(line)

    if deleted:
        print(f"Record for patient ID {patient_id} deleted.")
    else:
        print(f"No record found for patient ID {patient_id}.")

def main():
    while True:
        print("\n1. Add Patient\n2. View Patients\n3. Update Patient\n4. Delete Patient\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            name = input("Enter name: ")
            age = input("Enter age: ")
            gender = input("Enter gender: ")
            diagnosis = input("Enter diagnosis: ")
            treatment = input("Enter treatment plan: ")
            add_patient(patient_id, name, age, gender, diagnosis, treatment)
        elif choice == "2":
            view_patients()
        elif choice == "3":
            patient_id = input("Enter the patient ID to update: ")
            new_name = input("Enter new name (or leave blank): ") or None
            new_age = input("Enter new age (or leave blank): ") or None
            new_gender = input("Enter new gender (or leave blank): ") or None
            new_diagnosis = input("Enter new diagnosis (or leave blank): ") or None
            new_treatment = input("Enter new treatment plan (or leave blank): ") or None
            update_patient(patient_id, new_name, new_age, new_gender, new_diagnosis, new_treatment)
        elif choice == "4":
            patient_id = input("Enter the patient ID to delete: ")
            delete_patient(patient_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
