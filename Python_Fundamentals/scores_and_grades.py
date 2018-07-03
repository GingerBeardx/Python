import random
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score


def scores_and_grades(cases):
    count = 0
    while count < cases:
        random_num = random.randint(60, 100)
        print "Score:", random_num,
        if random_num >= 90:
            print "- Your grade is A"
        elif random_num >= 80:
            print "- Your grade is B"
        elif random_num >= 70:
            print "- Your grade is C"
        else:
            print "- Your grade is D"
        count += 1
    print "End of the program. Bye!"


scores_and_grades(10)
