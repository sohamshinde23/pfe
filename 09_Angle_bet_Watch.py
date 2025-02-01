# Input: Hours, Minutes, Seconds
H = int(input("Enter hours (0-11): "))
M = int(input("Enter minutes (0-59): "))
S = int(input("Enter seconds (0-59): "))

# Calculate the angle of the hour hand
angle = (30 * H) + (M * 0.5) + (S / 120)

# Output the result
print(f"The angle of the hour hand is: {angle:.2f} degrees")
