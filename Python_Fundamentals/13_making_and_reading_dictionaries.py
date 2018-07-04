# a dictionary with my info in it


""" print 'My name is', me['name']
print 'My age is', me['age']
print 'My country of birth is', me['country']
print 'My favorite language is', me['language']
 """


def print_dict_vals(me):
    for some_key, some_value in me.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)


print_dict_vals({'name': 'Eric', 'age': "35",
                 'country': 'United States of America', 'favorite language': 'Javascript'})
