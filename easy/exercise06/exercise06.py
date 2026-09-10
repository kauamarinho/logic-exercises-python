# Ask the user for a number N and display all numbers from 1 to N stating whether each is even or odd.

n = int(input("Enter a number: "))

even = n
odd = n

for i in range(n, n + 1):
    if n != even:
        print("The number is Odd")
    else:
        print("The number is Even")
