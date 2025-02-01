# Initialize a dictionary
student_grades = {'Alice': 85, 'Bob': 92}

# Insert a new key-value pair
student_grades['Charlie'] = 78
print("After insertion:", student_grades)

# Delete a key-value pair using del
del student_grades['Alice']
print("After deletion with del:", student_grades)

# Delete a key-value pair using pop and capture the removed value
removed_grade = student_grades.pop('Bob')
print("After deletion with pop:", student_grades)
print("Removed grade:", removed_grade)
