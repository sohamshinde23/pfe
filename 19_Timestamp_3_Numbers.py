# Input: Two timestamps
h1, m1, s1 = map(int, input("Enter the first timestamp (hours minutes seconds): ").split())
h2, m2, s2 = map(int, input("Enter the second timestamp (hours minutes seconds): ").split())

# Convert both timestamps to seconds from the start of the day
timestamp1_seconds = h1 * 3600 + m1 * 60 + s1
timestamp2_seconds = h2 * 3600 + m2 * 60 + s2

# Calculate the difference in seconds
difference = timestamp2_seconds - timestamp1_seconds

# Output the result
print("The difference in seconds is:", difference)