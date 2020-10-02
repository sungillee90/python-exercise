def score(total, correct, wrong):
    print("Total number of quizzes: " + str(total))
    print("Total number of  quizzes you correctly answered: " + str(correct))
    print("Total number of quizzes you answered incorrectly: " + str(wrong))
    total_points = (correct * 2 + wrong * 1)
    print("Total points: " + str(total_points))
    total_grade = (total_points / (total * 2)) * 100

    print("Total grade: " + str(total_grade))
    return total_grade
score(30,20,5)