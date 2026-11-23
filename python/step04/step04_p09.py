# Name: Adam Gavel
# Date: 11/23/2026
# Program Name: Problem 9: Positive or negative

number = 99

while number != 0:
    number = int(input("Enter a number (0 to stop): "))
    if number % 2 == 0 and number != 0:
        print("Positive")
    elif number != 0:
        print("Negative")

print("All done.")