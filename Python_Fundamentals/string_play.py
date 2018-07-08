# The point of this is to create a dictinoary and then add dictionaries to that dictionary for the Ninja Gold Assignment

session = {}
session['strings'] = {}


def create_string_dict():
    count = 0
    string = ''
    while count < 5:
        string = "The current string is number {}".format(count)
        session['strings'][count] = string
        count += 1
    return session['strings']

create_string_dict()
print session

def print_session():
    count = 0
    while count < 5:
        print session['strings'][count]
        count += 1


print_session()
        
