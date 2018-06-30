def checkers():
    string = "* * * *"
    for row in range(0, 8):
        if row % 2 == 0:
            print string
        else:
            print " " + string


checkers()
