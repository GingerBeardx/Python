# tuples are immuntable(unchangeable) and are enclosed in () rather than in [] like lists, which are mutable.
tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5)
tuple_letters = "a", "b", "c", "d"

# another example
dog = ("Canis Familiaris", "dog", "carnivore", 12)

print dog[2]
# result is: carnivore

for data in dog:
    print data
# prints all the items in the tuple

# dog[0] = "X"
# TypeError: 'tuple' object does not support item assignment

# Like strings, tuples are immutable. Once Python has created a tuple in memory, it cannot be changed. But we can add and slice tuples. See example below:
dog = dog + ("domestic",)
print dog
# result is...
# ("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
print dog
# result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

""" You may recognize some of these built-in functions for sequences:
max(sequence) returns the largest value in the sequence
sum(sequence) return the sum of all values in sequence
enumerate(sequence) used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence """
