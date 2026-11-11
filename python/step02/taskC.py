# Name: Adam Gavel
# Date: 11/11/2026
# Program Name: Paycheck Calculator
# Description: program that prints a weekly pay stub with taxes taken out, plus yearly totals.

FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

employee_name = input("Employee name: ")
hourly_rate = float(input("Hourly pay rate: "))
hours_worked_week = float(input("Hours worked this week: "))
print()

print("=" * 32)
print(f"PAY STUB: {employee_name}")
print("=" * 32)

print("Hours worked:\t" + str(hours_worked_week))
print("Hourly rate:\t$" + str(hourly_rate))
gross_pay = hourly_rate * hours_worked_week
print("Gross pay:\t$" + str(gross_pay))

print("-" * 32)
federal_tax = gross_pay * FEDERAL_TAX_RATE

print(f"Federal tax ({FEDERAL_TAX_RATE:.2%}):\t${federal_tax:.2f}")

state_tax = gross_pay * STATE_TAX_RATE
print(f"State tax ({STATE_TAX_RATE:.2%}):\t${state_tax:.2f}")

social_security = gross_pay * SOCIAL_SECURITY_RATE
print(f"Social Security:\t${social_security:.2f}")

medicare = gross_pay * MEDICARE_RATE
print(f"Medicare:\t        ${medicare:.2f}")

total = federal_tax + state_tax + social_security + medicare
print(f"Total taken out:\t${total:.2f}")
print("-" * 32)

net_pay = gross_pay - total
print(f"NET PAY:\t${net_pay}")
print("=" * 32)

print(f"You keep {(net_pay / gross_pay):.1%} of what you earn.")
print(f"Yearly gross: ${gross_pay * WEEKS_PER_YEAR:.2f}")
print(f"Yearly net: ${net_pay * WEEKS_PER_YEAR:.2f}")