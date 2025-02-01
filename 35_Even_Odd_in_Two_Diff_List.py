# Program to separate even and odd elements into two lists

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = [num for num in my_list if num % 2 == 0]
odd_list = [num for num in my_list if num % 2 != 0]

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
