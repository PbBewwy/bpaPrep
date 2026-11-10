# Name: Adam Gavel
# Date: 11/10/2026
# Program Name: Pizza Party Planner
# Description: Program that plans the pizza for a party.

slices_per_pizza = 8
pizza_price = 12.99
slice_price = 2.25

host_name = input("Host name: ")
num_people = int(input("Number of people: "))
slices_per = int(input("Slices per person: "))


print("\n=== Pizza Plan for " + host_name + "'s Party ===")
total_slices = num_people * slices_per

print("Slices needed:\t" + str(total_slices))
whole_pizzas = total_slices // slices_per_pizza

print("Whole pizzas:\t" + str(whole_pizzas))
extra_slices = total_slices % slices_per_pizza

print("Extra slices:\t" + str(total_slices % slices_per_pizza))
total_cost = round(whole_pizzas * pizza_price + extra_slices * slice_price, 2)

print("Total cost:\t$" + str(total_cost))
cost_per_person = round(total_cost / num_people, 2)

print("Cost per person:\t$" + str(cost_per_person))