# Name: Adam Gavel
# Date: 11/23/2026
# Program Name: Problem 5: Password checker

PASSWORD = "python123"

answer = ""

while answer != PASSWORD:
    answer = input("Enter the password: ")
    if answer != PASSWORD:
        print("Try again!")

print("Access granted!")