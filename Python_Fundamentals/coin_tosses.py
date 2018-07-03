import random
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score


def scores_and_grades(cases):
    count = 1
    heads = 0
    tails = 0
    result = ''
    while count <= cases:
        random_num = random.random()
        if round(random_num) == 1:
            heads += 1
            result = 'head'
        else:
            tails += 1
            result = 'tail'
        print "Attempt #", count, ": Throwing a coin... It's a", result, "! ... Got", heads, "head(s) so far and", tails, "tail(s) so far."
        count += 1
    print "Ending the progarm, thank you!"


scores_and_grades(5000)
