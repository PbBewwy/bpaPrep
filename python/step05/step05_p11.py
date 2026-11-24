# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 11: Bigger of two

def bigger(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return b

first = int(input("First number: "))
second = int(input("Second number: "))
print(f"The bigger number is {bigger(first, second)}")