# Name: Adam Gavel
# Date: 11/23/2026
# Program Name: Problem 11: Ask again until it is in range

answer = 111

while answer < 1 or answer > 10:
    answer = int(input("Rate the movie (1-10): "))
    if answer < 1 or answer > 10:
        print("Please answer 1 to 10.")

print(f"Your rating: {answer}")