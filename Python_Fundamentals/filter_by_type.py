sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1, 7, 4, 21]
mL = [3, 5, 7, 34, 3, 2, 113, 65, 8, 89]
lL = [4, 34, 22, 68, 9, 13, 3, 5, 7, 9, 2, 12, 45, 923]
eL = []
spL = ['name', 'address', 'phone number', 'social security number']


def tester(case):
    print case
    # first determine the data type
    if isinstance(case, int) == True:
        # then if integer is true - determine if the nubmer is big or small
        if case > 100:
            print "That is a big number!"
        else:
            print "That is a small number."
    elif isinstance(case, basestring) == True:
        # if string - determine if string is short or long
        if len(case) >= 50:
            print "Long sentence"
        else:
            print "Short sentence"
    elif isinstance(case, list) == True:
        # if list - determine if the list is big or short
        if len(case) >= 10:
            print "Big list!"
        else:
            print "Short list."
    """ print isinstance(sI, list)
    
    print isinstance(sI, basestring) """


tester(eS)
