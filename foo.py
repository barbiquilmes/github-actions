"""
This is a module that contains a function that adds two numbers or two strings.
"""


def add(first, second):
    """
    This function adds two numbers or two strings.
    :type a: int or str
    :type b: int or str
    """
    if isinstance(first, int) and isinstance(second, int):
        return first + second
    if isinstance(first, str) and isinstance(second, str):
        return first + " " + second

    return None
