# input
def findChar(lis, char):
    new_list = []
    for idx in lis:
        print idx
        if idx.find(char) == True:
            print idx
            new_list.append(idx)
    print new_list
    return new_list


findChar(['hello', 'world', 'my', 'name', 'is', 'Anna'], 'o')


# output
#new_list = ['hello', 'world']
