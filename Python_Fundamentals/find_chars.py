# input
def findChar(lis, char):
    new_list = []
    for idx in lis:
        if char in idx:
            new_list.append(idx)
    return new_list


findChar(['hello', 'world', 'my', 'name', 'is', 'Anna'], 'o')


# output
#new_list = ['hello', 'world']
