def add_nums(*num):
    """Add numbers together.

    :param int num: One or more numbers to add.
    :returns: The sum of all numbers provided.
    :rtype: int

    Example::
        >>> add_nums(2, 3, 5)
        10
    """
    sum = 0
    for n in num:
        sum = sum + n
    return sum
