# Take input from the user
P = float(input("Enter the principal amount: "))
T = float(input("Enter the time in years: "))
R = float(input("Enter the rate of interest: "))

# Calculate Simple Interest
simple_interest = (P * T * R) / 100

# Print the result
print(f"Simple Interest: {simple_interest}")