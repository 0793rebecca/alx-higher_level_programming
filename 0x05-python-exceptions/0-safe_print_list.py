#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print the first "x" elements of a list 'my_list'.

    my_list (list): The list of elements.
    x (int): The number of element to print.

    Return:
    the number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end=" ")
            count += 1
        except IndexError:
            break
    print()  # Print a new line after all elements are printed
    return count
