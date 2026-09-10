# Countdown

# Ask the user for a positive integer and display a countdown from N to 0.


number = int(input("Give me a number for the countdown to 0: "))

for number in range(number, 0, -1):
    print(number)
