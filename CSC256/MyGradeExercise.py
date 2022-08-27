# Author: Nakarin Philangam
# Class: CSC256.0001


def calculateMyGrade(assignments_score, midterm_score, final_score):
    assignments_weight = 30
    midterm_weight = 35
    final_weight = 35

    lab_average = (float(assignments_score) * assignments_weight) / 100
    midterm_average = (float(midterm_score) * midterm_weight) / 100
    final_average = (float(final_score) * final_weight) / 100

    average_grade = "{:.2f}".format(lab_average + midterm_average + final_average)

    return average_grade


def main():
    print("Welcome to My Grade Calculator")
    while True:
        labs_score = input("Enter your Assignments score: ")
        if not labs_score.isnumeric():
            print("Invalid. Please enter a number >= 0")
            continue
        else:
            break

    while True:
        midterm_score = input("Enter your Midterm Exam score: ")
        if not midterm_score.isnumeric():
            print("Invalid. Please enter a number >= 0")
            continue
        else:
            break

    while True:
        final_score = input("Enter your Final Exam score: ")
        if not final_score.isnumeric():
            print("Invalid. Please enter a number >= 0")
            continue
        else:
            break

    final_grade = calculateMyGrade(labs_score, midterm_score, final_score)
    print(" ")
    print("Your average grade is: ", final_grade)


if __name__ == "__main__":
    main()
