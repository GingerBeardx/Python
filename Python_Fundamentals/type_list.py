def tester(case):
    string = "String: "
    adds = 0
    strings = 0
    numbers = 0

    for element in case:
        print element
        # first determine the data type
        if isinstance(element, float) or isinstance(element, int) == True:
            adds += element
            numbers += 1
        elif isinstance(element, basestring) == True:
            # if string - determine if string is short or long
            string += element + " "
            strings += 1

    if strings > 0 and numbers > 0:
        print "The list you entered is of mixed types"
    elif strings > 0:
        print "The list you entered is of string type"
    elif numbers > 0:
        print "The list you entered is of integer type"
    print string
    print "Sum:", adds


case_1 = ['magical unicorns', 19, 'hello', 98.98, 'world']
case_2 = [2, 3, 1, 7, 4, 12]
case_3 = ['magical', 'unicorns']


tester(case_2)
