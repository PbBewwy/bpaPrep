# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 4: Average of three

def average_of_three(a, b, c):
    temp = a + b + c
    return temp / 3.0

score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))
print(f"Average: {average_of_three(score1, score2, score3):.1f}")