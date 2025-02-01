# Input: Coordinates of three known vertices
x1, y1 = map(int, input("Enter first vertex (x1 y1): ").split())
x2, y2 = map(int, input("Enter second vertex (x2 y2): ").split())
x3, y3 = map(int, input("Enter third vertex (x3 y3): ").split())

# Determine the missing x-coordinate
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

# Determine the missing y-coordinate
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

# Output the missing vertex
print(f"The fourth vertex is: ({x4}, {y4})")
