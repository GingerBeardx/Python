ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

drawer = ['documents', 'envelopes', 'pens']
# access the drawer with index of 0 and print value
print drawer[0]  # prints documents
# access the drawer with index of 1 and print value
print drawer[1]  # prints envelopes
# access the drawer with index of 2 and print value
print drawer[2]  # prints pens

x = [1, 2, 3, 4, 5]
x.append(99)
print x
# the output would be [1,2,3,4,5,99]

x = [99, 4, 2, 5, -3]
print x[:]
# the output would be [99,4,2,5,-3]
print x[1:]
# the output would be [4,2,5,-3];
print x[:4]
# the output would be [99,4,2,5]
print x[2:4]
# the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output 3

""" 
list.extend(list2) adds all values from a second sequence to the end of the original sequence.
list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
list.index(value) returns the index position in a list for the given parameter.
"""
