#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Parameters:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float: The result of the division or None if an exception occurs.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))

    return result
