# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.


def odd_even():
    # start a loop that counts from 1 to 2000
    for count in range(1, 2001):
        print "Number is", count,
        # determine if the current iteration of the loop is even or odd
        if count % 2 == 0:
            # if the iteration is even, print "Number is x. This is an even number."
            print "- This is an even number."
        else:
            # if the iteration is odd, print "Number is x. This is an odd number."
            print "- This is an odd number."


# odd_even()

# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.


def multiply(arr, num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr


a = [2, 4, 10, 16]
# b = multiply(a, 5)
# print b

# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list.


def layered_multiples(arr):
    new_array = []
    # begin a loop that will iterate over the list
    for idx in arr:
        # determine the multiple of '1' to print
        new_item = []
        for count in range(0, idx):
            # create a list with the '1's
            new_item.insert(count - 1, 1)
        # insert that list into the new_array
        new_array.insert(idx - 1, new_item)
    # return new_array
    return new_array


x = layered_multiples(multiply([2, 4, 5], 3))
print x
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
