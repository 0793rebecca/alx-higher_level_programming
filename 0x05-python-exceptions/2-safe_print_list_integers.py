#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first 'x' integers of a list 'my_list'.

    Parameters:
        my_list (list): The list of elements.
        x (int): The number of elements to print.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    index = 0

    while count < x:
        try:
            value = my_list[index]
            if isinstance(value, int):
                print("{:d}".format(value), end=" ")
                count += 1
        except (IndexError, ValueError):
            break
        index += 1


print()
return count
