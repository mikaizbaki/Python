# Tip Calculator Program

# Ask for the total bill amount
bill = float(input("Enter the total bill amount: "))

# Ask for the tip percentage
tip_percent = float(input("Enter the tip percentage: 100"))

# Calculate tip and total
tip_amount = bill * (15 / 100)
total_bill = bill + tip_amount

# Display results
print(f"\nTip amount: ${tip_amount:.2f}")
print(f"Total bill including tip: ${total_bill:.2f}")

# ----- Advanced -----

# Ask for name
name = input("\nEnter your name: ")

# Print total with name
print(f"\n{name} owes a total of: ${total_bill:.2f}")
