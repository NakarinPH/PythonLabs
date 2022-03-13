# Nakarin Philangam
# 01/22/2022

class Student(object):
    """Represents a student."""

    def __init__(self, name="", numberOfScores=3):
        """All scores are initially 0."""
        self.name = name
        self.numberOfScores = [0, 0, 0]

    def display(self):
        """Display name, scores, highest and average score of the student."""
        highest_score = float(max(self.numberOfScores))
        average_score = sum(self.numberOfScores) / len(self.numberOfScores)
        print("Name: " + str(self.name))
        print("Scores: " + str(self.numberOfScores[0]) + " " + str(self.numberOfScores[1]) + " " + str(
            self.numberOfScores[2]))
        print("Highest score: %.2f" % highest_score)
        print("Average score: %.2f\n" % average_score)

    def getNumberOfScores(self):
        """Returns the number of scores."""
        return self.numberOfScores

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 0."""
        self.numberOfScores[i] = score

    def getScore(self, i):
        """Returns the ith score, counting from 0."""
        return self.numberOfScores[i]

    def getAverage(self):
        """Returns the average score."""
        average = sum(self.numberOfScores) / len(self.numberOfScores)
        return average

    def getHighScore(self):
        """Returns the highest score."""
        highest = float(max(self.numberOfScores))
        return highest


from random import randint


def main(numScores=3):
    """Tests sorting."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:\n")
    for s in students:
        s.display()


if __name__ == "__main__":
    main()
