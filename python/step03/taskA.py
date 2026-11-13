# Name: Adam Gavel
# Date: 11/12/2026
# Program Name: Movie Ticket Price
# Description: A program that figures out the price of one movie ticket.

CHILD_PRICE = 7.00
ADULT_PRICE = 11.00
SENIOR_PRICE = 8.00
TUESDAY_DISCOUNT = 3.00
THREE_D_CHARGE = 2.50

# Input
name = input("Name: ")
age = int(input("Age: "))
dotw = input("Day of the week: ")
movie = input("3D movie? (y/n): ")

# Processing
if age < 0 or age > 120:
    print("Error: age must be 0 to 120.")
else:
    if age < 13:
        base_price = CHILD_PRICE
        agetype = "Child"
    elif age >= 65:
        base_price = SENIOR_PRICE
        agetype = "Senior"
    else:
        base_price = ADULT_PRICE
        agetype = "Adult"

    total = base_price
    is_tuesday = dotw.lower() == "tuesday"
    is_3d = movie.lower() == "y"

    if is_tuesday:
        total -= TUESDAY_DISCOUNT

    if is_3d:
        total += THREE_D_CHARGE

    # Output
    print()
    print(f"--- Ticket for {name} ---")
    print(f"Ticket type:   {agetype}")
    print(f"Base price:    ${base_price:.2f}")

    if is_tuesday:
        print(f"Tuesday deal: -${TUESDAY_DISCOUNT:.2f}")

    if is_3d:
        print(f"3D charge:     ${THREE_D_CHARGE:.2f}")

    print(f"Total:         ${total:.2f}")