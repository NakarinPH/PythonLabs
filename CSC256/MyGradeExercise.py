# Author: Nakarin Philangam
# Class: CSC256.0001


def calculateMyGrade(labs_score, midterm_score, final_score):
    labs_weight = 34
    midterm_weight = 33
    final_weight = 33

    lab_average = (labs_score * labs_weight) / 100
    midterm_average = (midterm_score * midterm_weight) / 100
    final_average = (final_score * final_weight) / 100

    average_grade = "{:.2f}".format(lab_average + midterm_average + final_average)

    return average_grade


def main():
    print("Welcome to My Grade Calculator")
    labs_score = float(input("Enter your labs score: "))
    midterm_score = float(input("Enter your midterm score: "))
    final_score = float(input("Enter your final score: "))
    final_grade = calculateMyGrade(labs_score, midterm_score, final_score)
    print(" ")
    print("Your average grade is: ", final_grade)


if __name__ == "__main__":
    main()
