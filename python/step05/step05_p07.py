# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 7: Tip calculator

def calculate_tip(bill, percent):
    return bill * (percent / 100)

bill = float(input("Bill amount: "))
tip_percent = float(input("Tip percent: "))
print(f"Tip: ${calculate_tip(bill, tip_percent):.2f}")
print(f"Total: ${bill + calculate_tip(bill, tip_percent):.2f}")