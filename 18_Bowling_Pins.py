# Input: Number of pins (N) and number of balls (K)
N = int(input())
K = int(input())

# Initialize the pins, all pins are standing initially
pins = ['I'] * N

# Process each ball's knocked-down pins
for _ in range(K):
    start, end = map(int, input().split())
    for i in range(start - 1, end):
        pins[i] = '.'  # Knock down the pins

# Output the final pin state
print("".join(pins))
