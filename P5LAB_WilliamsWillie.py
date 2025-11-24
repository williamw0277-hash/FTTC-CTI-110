# Willie Williams
# 11/24/2025
# P5LAB - Self-Checkout Change Dispenser
# This program simulates a self-checkout machine. A random purchase total
# is generated, the user enters their payment, and the program calculates
# and displays the dollars and coins required to make change.

import random

def disperse_change(change_amount):
    """
    Takes the change owed (float) and prints the breakdown of dollars,
    quarters, dimes, nickels, and pennies. No return value.
    """

    # Convert to cents to avoid floating-point issues
    cents = round(change_amount * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print("\nChange Owed Breakdown:")
    print(f"Dollars  : {dollars}")
    print(f"Quarters : {quarters}")
    print(f"Dimes    : {dimes}")
    print(f"Nickels  : {nickels}")
    print(f"Pennies  : {pennies}")


def main():
    # Generate random purchase total
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Amount owed: ${amount_owed}")

    # Get payment from user
    user_cash = float(input("Enter the amount of cash given: $"))

    # Calculate change
    change = round(user_cash - amount_owed, 2)

    # If not enough money is provided
    if change < 0:
        print(f"\nERROR: Insufficient funds. You still owe ${abs(change):.2f}.")
        return

    print(f"\nChange owed: ${change:.2f}")

    # Call function to disperse the change
    disperse_change(change)


# Run the program
main()
