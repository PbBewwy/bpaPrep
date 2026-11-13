# Name: Adam Gavel
# Date: 11/13/2026
# Program Name: Shipping Calculator
# Description: A program that figures out the shipping cost and delivery time for an online order.

ZONE1_RATE = 0.50
ZONE2_RATE = 0.75
ZONE3_RATE = 1.25
MINIMUM_SHIPPING =  4.00
FREE_SHIPPING_AMOUNT = 50.00
RUSH_FEE = 10.00

# Input
order_total = float(input("Order total: "))
package_weight_pounds = float(input("Package weight (lbs): "))
shipping_zone = int(input("Shipping zone (1-3): "))
rush_delivery = input("Rush delivery? (y/n): ")

# Processing
if order_total <= 0 or package_weight_pounds <= 0:
    print("Error: order total and weight must be more than 0.")
elif shipping_zone != 1 and shipping_zone != 2 and shipping_zone != 3:
    print("Error: zone must be 1, 2, or 3.")
else:
    shipping = 0
    is_rush = False
    is_heavy = False
    days = 0

    if shipping_zone == 1:
        shipping = package_weight_pounds * ZONE1_RATE
        days = 2
    if shipping_zone == 2:
        shipping = package_weight_pounds * ZONE2_RATE
        days = 4
    if shipping_zone == 3:
        shipping = package_weight_pounds * ZONE3_RATE
        days = 6

    if shipping < 4.00:
        shipping = MINIMUM_SHIPPING

    if rush_delivery.lower() == "y":
        is_rush = True
        if shipping_zone == 1:
            days = 1
        if shipping_zone == 2:
            days = 1
        if shipping_zone == 3:
            days = 2

    if order_total >= FREE_SHIPPING_AMOUNT and not is_rush:
        shipping = 0

    if is_rush:
        shipping += RUSH_FEE

    if package_weight_pounds > 50:
        days += 2
        is_heavy = True

    # Output
    print("--- Shipping Summary ---")
    print(f"Order total:  ${order_total:.2f}")
    if shipping != 0:
        print(f"Shipping:     ${shipping:.2f}")
    else:
        print("Shipping:     FREE")
    print(f"Grand total:  ${(shipping + order_total):.2f}")
    if days == 1:
        print(f"Arrives in:   1 day")
    else:
        print(f"Arrives in:   {days} days")
    if is_heavy:
        print("Note: heavy package, 2 extra days added.")