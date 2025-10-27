# Willie Williams
# October 27, 2025
# P4LAB2 - Multiplication Table
# This program asks the user for an integer and displays
# its multiplication table from 1 to 12 using loops.
# If the number is negative, it tells the user it cannot accept it.
# The program repeats until the user chooses to stop.

# Main program loop (while loop)
run_again = "yes"

while run_again.lower() == "yes":
    # Ask user for an integer
    number = int(input("Enter an integer: "))

    # Check for non-negative integer
    if number >= 0:
        print(f"\nMultiplication table for {number}")
        print("-------------------------------")

        # Display multiplication table (for loop)
        for i in range(1, 13):
            result = number * i
            print(f"{number} x {i} = {result}")
    else:
        print("Sorry, I cannot accept negative values.")

    # Ask user if they wish to run again
    run_again = input("\nWould you like to run the program again? (yes/no): ")

print("\nThank you for using the multiplication table program!")
