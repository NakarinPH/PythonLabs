# Nakarin Philangam
# 01/06/2022

# Get inputs from the user
height = float(input("Enter the height from which the ball is dropped: "))
index = float(input("Enter the bounciness index of the ball: "))
times = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

# Declare the total
total = 0

# Use for loop to calculate the total
for num in range(times):
    total += (height + index * height)
    height = index * height
# Display the total
print("Total distance traveled is:", total, "units.")
