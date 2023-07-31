#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().
    Otherwise, returns False.

    Parameters:
        value: The value to be printed.

    Returns:
        bool: If a TypeError or ValueError occurs - False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
