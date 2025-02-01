import math

# Input coefficients from the user
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)    
    print("The roots are real and distinct:", root1, "and", root2)
elif discriminant == 0:
    # One real root
    root = -b / (2 * a)
    print("The root is real and unique:", root)
else:
    # No real roots (complex roots)
    print("The equation has no real roots")