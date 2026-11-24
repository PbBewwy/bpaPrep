# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 12: Use main()

def calculate_total(price, quantity):
    return quantity * price

def main():
    name = input("Item: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    print(f"{quantity} {name} cost ${calculate_total(price, quantity):.2f}")

if __name__ == "__main__":
    main()