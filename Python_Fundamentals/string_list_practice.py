# find and replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
words = "It's Thanksgiving day. It's my birthday, too!"
x = words.find("day")
""" print x """
words = words.replace("day", "month")
""" print words """

# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2, 54, -2, 7, 12, 98]
""" print max(x)
print min(x) """

# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
""" print x[0]
print x[len(x)-1] """

first = x[0]
last = x[len(x)-1]
y = [first, last]
""" print y """

# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
print x

first_list = x[:len(x)/2]  # optional first parameter of slice defaults to zero
# optional second parameter of slice defaults to the list's length
second_list = x[len(x)/2:]
print "first list", first_list
print "second_list", second_list
second_list.insert(0, first_list)
print second_list
