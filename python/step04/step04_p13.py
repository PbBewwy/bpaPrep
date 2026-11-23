# Name: Adam Gavel
# Date: 11/23/2026
# Program Name: Problem 13: Count and add until zero

total = 0
answer = 5
total_numbers = 0

while answer != 0:
    answer = int(input("Enter a number (0 to stop): "))
    total_numbers += 1
    total += answer

print(f"You entered {total_numbers - 1} numbers.")
print(f"The total is {total}")