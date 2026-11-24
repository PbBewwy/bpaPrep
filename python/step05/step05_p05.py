# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 5: Even or odd

def is_even(number):
    return number % 2 == 0

number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")