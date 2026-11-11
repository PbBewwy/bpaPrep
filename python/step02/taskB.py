# Name: Adam Gavel
# Date: 11/10/2026
# Program Name: Road Trip Calculator
# Description: Program that calculates gas, cost per person, and driving time for a road trip.

AVERAGE_SPEED = 55

destination = input("Destination: ")
trip_distance = float(input("Trip's distance: (miles): "))
miles_per_gallon = float(input("Car's miles per gallon: "))
gas_per_gallon = float(input("Gas price per gallon: "))
num_people_split = int(input("Number of people splitting the cost: "))
print()

print("--- Trip to " + destination + " ---")
gallons_of_gas = round(trip_distance / miles_per_gallon, 1)
print("Gallons of gas:\t" + str(gallons_of_gas))
gas_cost = round(gallons_of_gas * gas_per_gallon, 2)
print("Gas gost:\t$" + str(gas_cost))
cost_per_person = round(gas_cost / num_people_split, 2)
print("Cost per person:\t$" + str(cost_per_person))
driving_time = int(trip_distance / AVERAGE_SPEED * 60)
print("Driving time:\t" + str(driving_time // 60) + " hr " + str(driving_time % 60) + " min (at " + str(AVERAGE_SPEED) + " mph)")
round_trip = round(gas_cost * 2, 2)
print("Round trip gas:\t$" + str(round_trip))