# Name: Adam Gavel
# Date: 11/23/2026
# Program Name: Problem 10: Average of five test scores

total = 0

for i in range (1, 6):
    total += float(input("Test score: ")) 

total = total / 5
print(f"Average: {total}")