print "this is a sample string"

name = "Zen"
print "My name is", name

name = "Yen"
print "My name is " + name

integer = 42
print "The number I am thinking of is", integer

integer_2 = 68
# The following line will not work as Python cannot concatenate 'str' and 'int' objects
# print "Just kidding, I am really thinking of " + integer_2

first_name = "Zen"
last_name = "Coder"
# using {} to inject variables into the string is known as string interpolation.
print "My name is {} {}".format(first_name, last_name)

'''
string.count(substring): returns number of occurrences of substring in string.
string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.
string.find(substring): returns the index of the start of the first occurrence of substring within string.
string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
string.split(): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
'''
