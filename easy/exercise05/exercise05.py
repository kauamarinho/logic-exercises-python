# Read 5 numbers from the user and report which was the largest and the smallest among them

first = int(input("Enter the 1st number: "))
largest = first
smallest = first

for i in range(2, 6):
    number = int(input(f"Enter the {i}th number: "))

    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print(f"\nLargest number: {largest}")
print(f"Smallest number: {smallest}")
