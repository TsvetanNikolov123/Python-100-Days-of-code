# Welcome message to introduce the program
print("Welcome to the tip calculator!")

# Get the total bill amount from user as a float (allows decimal values like $25.50)
bill = float(input("What was the total bill? $"))

# Get the tip percentage as an integer (common values: 10%, 12%, 15%)
tip = int(input("What percentage tip would you like to give? 10 12 15 "))

# Get the number of people to split the bill between
people = int(input("How many people to split the bill? "))

# Calculate the total bill including tip
# Formula: (tip percentage / 100) * original bill + original bill
# Example: If bill=$100 and tip=15%, then: (15/100)*100 + 100 = 15 + 100 = $115
bill_with_tip = tip / 100 * bill + bill

# Display the total bill with tip, rounded to 2 decimal places (standard currency format)
# Note: This shows the TOTAL bill, not the amount per person
print(round(bill_with_tip, 2))