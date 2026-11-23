# Name: Adam Gavel
# Date: 11/23/2026
# Program Name: Problem 7: Add numbers until zero

total = 0
answer = 5

while answer != 0:
    answer = int(input("Enter a number (0 to stop): "))
    total += answer

print(f"The total is {total}")