# Willie Williams
# October 23, 2025
# P3HW2 - Salary
# This program calculates an employee's pay, including overtime,
# based on hours worked and pay rate. It displays the breakdown of
# regular pay, overtime pay, and total gross pay.
# --------------------------------------------------------
# Pseudocode (Detailed Algorithm)
# --------------------------------------------------------
# 1. Ask user for employee name.
# 2. Ask for number of hours worked.
# 3. Ask for employee's pay rate.
# 4. Determine if hours worked > 40:
#    a. If yes, calculate overtime hours = hours_worked - 40
#       and regular hours = 40.
#    b. Otherwise, overtime hours = 0 and regular hours = hours_worked.
# 5. Calculate:
#    - Regular pay = regular hours * pay rate
#    - Overtime pay = overtime hours * (pay rate * 1.5)
#    - Gross pay = regular pay + overtime pay
# 6. Display a nicely formatted pay summary:
#    - Employee name
#    - Pay rate
#    - Hours worked
#    - Overtime hours
#    - Overtime pay
#    - Regular pay
#    - Gross pay
# --------------------------------------------------------

# Input section
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Processing
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

# Output
print("\n----------------------------------------")
print(f"Employee name: {employee_name}")
print("----------------------------------------")
print(f"Pay Rate:        ${pay_rate:10.2f}")
print(f"Hours Worked:    {hours_worked:10.2f}")
print(f"Overtime Hours:  {overtime_hours:10.2f}")
print(f"Overtime Pay:    ${overtime_pay:10.2f}")
print(f"Regular Pay:     ${regular_pay:10.2f}")
print("----------------------------------------")
print(f"Gross Pay:       ${gross_pay:10.2f}")
print("----------------------------------------")
