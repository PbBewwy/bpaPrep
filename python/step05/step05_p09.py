# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 9: Rectangle area and perimeter

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return (width * 2) + (height * 2)

width = float(input("Width: "))
height = float(input("Height: "))

print(f"Area: {calculate_area(width, height)}")
print(f"Perimeter: {calculate_perimeter(width, height)}")