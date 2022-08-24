# Author: Nakarin Philangam
# Class: CSC256.0001


def calculateMyGrade(assignments_score, midterm_score, final_score):
    assignments_weight = 30
    midterm_weight = 35
    final_weight = 35

    lab_average = (assignments_score * assignments_weight) / 100
    midterm_average = (midterm_score * midterm_weight) / 100
    final_average = (final_score * final_weight) / 100

    average_grade = "{:.2f}".format(lab_average + midterm_average + final_average)

    return average_grade


def main():
    print("Welcome to My Grade Calculator")
    labs_score = float(input("Enter your Assignments score: "))
    midterm_score = float(input("Enter your Midterm Exam score: "))
    final_score = float(input("Enter your Final Exam score: "))
    final_grade = calculateMyGrade(labs_score, midterm_score, final_score)
    print(" ")
    print("Your average grade is: ", final_grade)


if __name__ == "__main__":
    main()
