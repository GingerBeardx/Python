list_one_a = [1, 2, 3, 6, 2]
list_two_a = [1, 2, 3, 6, 2]

list_one_b = [1, 2, 5, 6, 5]
list_two_b = [1, 2, 5, 6, 5, 3]

list_one_c = [1, 2, 5, 6, 5, 16]
list_two_c = [1, 2, 5, 6, 5]

list_one_d = ['celery', 'carrots', 'bread', 'milk']
list_two_d = ['celery', 'carrots', 'bread', 'cream']


def compare_Lists(li1, li2):
    if len(li1) > len(li2) or len(li1) < len(li2):
        return "The lists are not the same"

    for idx in range(len(li1)):
        if li1[idx] != li2[idx]:
            return "The lists are not the same"
    return "The lists are the same"


print compare_Lists(list_one_d, list_two_d)
