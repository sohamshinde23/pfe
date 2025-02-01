set1 = {1, 2, 3, 4}
set2 = {3, 5, 7, 8}

if set1 & set2:
    print("The sets have common elements.")
else:
    print("The sets do not have any common elements.")



#user input
set1 = set(input("Enter elements of the first set: ").split())
set2 = set(input("Enter elements of the second set: ").split())

if set1 & set2:
    print("The sets have common elements.")
else:
    print("The sets do not have any common elements.")