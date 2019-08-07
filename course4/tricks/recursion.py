# Recursion:

# Run this in pythontutor.com
def factorial(n):  # This function is recursive, it calls itself (but this is VERY-VERY-VERY-VERY STUPID EXAMPLE).
    if n == 0:
        return 1

    return n * factorial(n - 1)
    #return factorial(fgh)






#4 * 3 * 2 * 1
#4 * (3 * (2 * 1))
print(factorial(4))  # 4 * 3 * 2 * 1 = 24









print(factorial(4000))







import sys
sys.getrecursionlimit()


# More realistic example

def double_all_elements(lst):
    if len(lst) == 0:
        return []
    else:
        updated_element = lst[0] * 2
        print(updated_element, len(lst))
        result = [updated_element, ] \
                 + double_all_elements(lst[1:])
    return result


# Convert to tail recursion

def double_all_elements(lst, result_lst=None):
    """ Double all elements in list (tail recursion example)
    :param lst: incoming list
    :return: result list
    """

    if result_lst == None:
        result_lst = []

    if len(lst) == 0:
        return result_lst
    else:
        updated_element = lst[0] * 2
        result_lst.append(updated_element)
        print(updated_element, len(lst), result_lst)
        result = double_all_elements(lst[1:], result_lst)
        #print(result)
    return result


# Convert recursion to loop
def double_all_elements(lst, result_lst=None):
    """  Double all elements in list (without recursion)
    :param lst: incoming list
    :return: result list
    """

    if result_lst == None:
        result_lst = []

    while len(lst) > 0:
        updated_element = lst[0] * 2
        print(updated_element, len(lst), result_lst)
        (lst, result_lst) = (lst[1:], result_lst + [updated_element, ])
    return result_lst


def print_all_list_items(data):
    if not data:
        return 
    item = data.pop()
    print(item)
    return print_all_list_items(data)

print_all_list_items(['1', '2', 'end'])
