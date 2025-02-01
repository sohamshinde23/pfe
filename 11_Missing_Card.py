# Input N
N = int(input())

# Read N-1 numbers and compute their sum
total_sum = sum(map(int, input().split()))

# Compute the expected sum of all numbers from 1 to N
expected_sum = N * (N + 1) // 2

# Find the missing number
missing_number = expected_sum - total_sum

# Output the missing number
print(missing_number)