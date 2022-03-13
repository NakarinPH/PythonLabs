# Nakarin Philangam
# 01/14/2022

# Create an empty list
course = []

# Loop to continue the program
user_input = 'A', 'D'

while user_input:

    # Promp the user for an input
    user_input = input("Enter A to add course, D to drop course, and E to exit: ")

    if user_input == 'A' or user_input == 'a':
        course_to_add = input("Enter course to add: ")
        if course_to_add in course:
            print("You are already registered in that course")
        else:
            course.append(course_to_add)
            print("Course added")
            course.sort()
            print("Course registered:", course)
    elif user_input == 'D' or user_input == 'd':
        course_to_drop = input("Enter course to drop: ")
        if course_to_drop in course:
            course.remove(course_to_drop)
            print("Course dropped")
            course.sort()
            print("Course registered:", course)
        else:
            print("You are not registered in that course")
    elif user_input == 'E' or user_input == 'e':
        exit()
    else:
        print("Invalid input")
        continue





