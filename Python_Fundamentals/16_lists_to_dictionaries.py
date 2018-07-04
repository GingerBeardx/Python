name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider",
                   "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(list_one, list_two):
    if len(list_one) < len(list_two):
        tups = zip(list_two, list_one)
    else:
        tups = zip(list_one, list_two)
    print tups
    new_dict = dict(tups)
    return new_dict


# print make_dict(name, favorite_animal)

# Optimized:

def making_dictionaries(list1, list2):
    the_dict = {}
    for i in range(0, len(list1)):
        the_dict[list1[i]] = list2[i]
    return the_dict


print making_dictionaries(name, favorite_animal)
