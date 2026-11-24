# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 6: Letter grade

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    else:
        return "F"


score = int(input("Score: "))
print(f"Letter grade: {letter_grade(score)}")