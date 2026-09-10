
# Ask the user how many numbers they want to add. Read each number and display the total sum at the end.

n = int(input("How many numbers do you want to add? "))

total = 0

for i in range(1, n + 1):
    number = float(input(f"Enter the {i}th number: "))
    total = total + number

print(f"\nThe sum of the {n} numbers is: {total}")
