# Define a password in the code. Ask the user to type it in.
# While they get it wrong, keep asking. Display a welcome message when they get it right.


password = 1234

user_password = int(input("Please enter your password: "))

while user_password != password:
    print("Incorrect password! Try again.")
    user_password = int(input("Please enter your password: "))
else:
    print("Correct password!")
