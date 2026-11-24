# Name: Adam Gavel
# Date: 11/24/2026
# Program Name: Problem 10: Temperature table

def to_fahrenheit(celcius):
    return (celcius * 9 / 5 + 32)

print("Celcius\tFahrenheit")
for i in range(0, 101, 20):
    print(f"{i}\t{to_fahrenheit(i)}")