# Willie C. Williams Jr.
# 2025-11-03
# P4HW2 - Payroll Calculator with Overtime & Totals
# This program repeatedly collects employee payroll info until the user enters "Done" for name.
# For each employee, it computes regular pay and overtime pay (time-and-a-half for hours > 40),
# shows a per-employee breakdown, and tracks totals for overtime, regular, and gross pay,
# plus the total number of employees processed.

"""
Pseudocode (Detailed Algorithm)
-------------------------------
1) Display a brief title/banner (optional).
2) Initialize accumulator variables:
     total_overtime_pay = 0.0
     total_regular_pay  = 0.0
     total_gross_pay    = 0.0
     employee_count     = 0
3) LOOP forever:
     - Prompt for employee name: name = input("Enter employee's name or Done to terminate: ")
     - IF name == "Done":
           break the loop (stop entering employees)
     - Prompt for hours worked (float) with validation (must be >= 0)
     - Prompt for pay rate (float) with validation (must be >= 0)

     - Compute regular hours and overtime hours:
           if hours > 40:
               reg_hours = 40
               ot_hours  = hours - 40
           else:
               reg_hours = hours
               ot_hours  = 0

     - Compute pays:
           reg_pay = reg_hours * rate
           ot_pay  = ot_hours * rate * 1.5
           gross   = reg_pay + ot_pay

     - Print a formatted breakdown for this employee.

     - Update totals:
           total_overtime_pay += ot_pay
           total_regular_pay  += reg_pay
           total_gross_pay    += gross
           employee_count     += 1

4) After the loop ends (user entered "Done"):
     - Print a summary section:
           number of employees
           total overtime pay
           total regular pay
           total gross pay
5) End.
"""

def get_non_negative_float(prompt):
    """Prompt until a non-negative float is entered."""
    while True:
        entry = input(prompt)
        try:
            value = float(entry)
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 40 or 37.5).")

def main():
    print("P4HW2 - Payroll Calculator")
    print("-" * 40)

    total_overtime_pay = 0.0
    total_regular_pay  = 0.0
    total_gross_pay    = 0.0
    employee_count     = 0

    while True:
        name = input("\nEnter employee's name or Done to terminate: ")
        if name == "Done":
            break  # Only terminates if the user enters exactly "Done"

        hours = get_non_negative_float("Enter number of hours worked: ")
        rate  = get_non_negative_float("Enter pay rate: ")

        # Determine regular vs overtime hours
        if hours > 40:
            reg_hours = 40.0
            ot_hours  = hours - 40.0
        else:
            reg_hours = hours
            ot_hours  = 0.0

        reg_pay = reg_hours * rate
        ot_pay  = ot_hours * rate * 1.5
        gross   = reg_pay + ot_pay

        # Per-employee breakdown
        print("\nPay for:", name)
        print("Hours Worked   Pay Rate   Overtime   Overtime Pay   Regular Pay   Gross Pay")
        print("----------------------------------------------------------------------------")
        print(f"{hours:12.2f} {rate:10.2f} {ot_hours:10.2f} {ot_pay:14.2f} {reg_pay:13.2f} {gross:11.2f}")

        # Update totals
        total_overtime_pay += ot_pay
        total_regular_pay  += reg_pay
        total_gross_pay    += gross
        employee_count     += 1

    # Final summary
    print("\n============= Summary Totals =============")
    print(f"Number of employees entered : {employee_count}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular : ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross    : ${total_gross_pay:.2f}")
    print("==========================================")

if __name__ == "__main__":
    main()
