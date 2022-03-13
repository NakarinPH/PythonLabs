# Nakarin Philangam
# 01/14/2022
import statistics

# Create a list
numList = [27, 5, 18, 66, 12, 5, 9]

# Calculate the sum
total = sum(numList)

# Display the result
print("List: ", numList)
print("Median: ", statistics.median(numList))
print("Mean: ", total / len(numList))
