# Nakarin Philangam
# 01/14/2022

# Open the file to read the data
my_file = open('payroll_data.txt', 'r')

# Display the header
print("Name\t\tRate\t\tHours\t\tTotal Pay")

# Use for loop to get data
for line in my_file.readlines():
    cols = line.strip().split()
    name = cols[0]
    rate = float(cols[1])
    hours = float(cols[2])
    total = rate * hours
    print("%s\t\t%.2f\t\t%.2f\t\t%.2f" % (name, rate, hours, total))

# Close the file
my_file.close()
