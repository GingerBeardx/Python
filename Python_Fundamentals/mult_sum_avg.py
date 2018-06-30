# MULTIPLES

# Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.


def print_num():
    for idx in range(1, 1001):
        print idx


# print_num()


# Create another program that prints all the multiples of 5 from 5 to 1,000,000
def multiples_of_five():
    for idx in range(5, 1000000):
        if idx % 5 == 0:
            print idx


# multiples_of_five()

def sum_list():
    a = [1, 2, 5, 10, 255, 3]
    add = 0
    for element in a:
        add += element
    print add


# sum_list()

def avg_list(list_avg):
    add = 0
    for element in list_avg:
        add += element
    print add / len(list_avg)


# avg_list([1, 2, 5, 10, 255, 3])
