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
     ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
