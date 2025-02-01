# Input: String
s = input("Enter a string: ")

# Remove characters at indices divisible by 3
result = ''.join([s[i] for i in range(len(s)) if i % 3 != 0])

# Output: Modified string
print("Modified string:", result)