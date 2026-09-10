# Multiplication table

# Ask for a number and display its full multiplication table (from 1 to 10).

n = int(input("Enter a number: "))

print(f"\nMultiplication table of {n}:")

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
