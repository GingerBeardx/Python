
def mult_table():
    #print x
    print "x   ",
    # print the column headers 1-12
    for col_ind in range(1, 13):
        print col_ind, "  ",
    print "\n"
    # print the row head (left justified)
    for row_ind in range(1, 13):
        print row_ind, " ",
        # print the multiples
        for mult_int in range(1, 13):
            print " ", row_ind * mult_int,
        print "\n"
        # loop through and print the next row


mult_table()
