# Name: Adam Gavel
# Date: 11/13/2026
# Program Name: BPA Eligibility Checker
# Description: A program a chapter advisor could use to check whether a member can compete at BPA.

# Constants
MIN_GPA = 2.0
OFFICER_GPA = 2.0
HONOR_GPA = 3.5
MAX_EVENTS = 2

# Input
name = input("Member name: ")
grade = int(input("Grade (9-12): "))
gpa = float(input("GPA (0.0-4.0): "))
dues_paid = input("Dues paid? (y/n): ")
events_signed_for = int(input("Events signed up for: "))
print()

# Processing
if 9 <= grade <= 12:
    if 0.0 <= gpa <= 4.0:
        eligibility = True
        did_pay = True
        gpa_eligible = True
        if dues_paid.lower() != "y":
            eligibility = False
            did_pay = False
        if gpa <= 2.0:
            eligibility = False
            gpa_eligible = False

        # Output
        print(f"--- BPA Check for {name} ---")

        if eligibility:
            print("Status: ELIGIBLE")

            if events_signed_for == 0:
                print("Sign up for at least one event.")
            elif events_signed_for == 1:
                print("You are entered for 1 event.")
            elif events_signed_for == 2:
                print("You are entered in 2 events.")
            else:
                print(f"You can only enter 2 events. Drop {events_signed_for - 2}.")

            if grade == 11 or grade == 12:
                if gpa >= 3.0:
                    print("You can run for chapter office.")

            if grade == 12:
                if gpa >= 3.5:
                    print("Senior honor cord: yes")

        else:
            print("Status: NOTE ELIGIBLE")
            if did_pay != True:
                print("Reason: dues not paid.")
            if gpa_eligible != True:
                print("Reason: GPA is below 2.0.")
        
    else:
        print("Error: GPA must be 0.0 to 4.0.")
else:
    print("Error: grade must be 9 to 12.")