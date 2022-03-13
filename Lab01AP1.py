# Nakarin Philangam
# 01/06/2022

# Get the hour wage rate from the user
hour_wage = float(input("Enter hourly wage: $"))
# Get the number of hour that the user work in a week
hour_regular = int(input("Enter the regular hours: "))
# Get the number of overtime that the user work in a week
overtime_hour = int(input("Enter the overtime hours: "))

# Calculate the overtime rate
overtime_wage = hour_wage * 1.5
# Calculate the total that the user will be paid
total_week_pay = (hour_wage * hour_regular) + (overtime_hour * overtime_wage)

# Display the amount that the user needs to be paid
print("The total weekly pay is $%-6.1f" % total_week_pay)


