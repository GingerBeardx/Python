for count in range(0, 5):
    print "looping - ", count

# create a new list
# remember lists can hold many data-types, even lists!
my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world!']
for element in my_list:
    print element

count = 0
while count < 5:  # notice the colon!
    print 'looping - ', count
    count += 1
