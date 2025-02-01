
set1 = set(input("Enter elements of the first set: ").split())
set2 = set(input("Enter elements of the second set: ").split())

set1.intersection_update(set2)

print("Updated set1 with common elements:", set1)