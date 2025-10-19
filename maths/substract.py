def subtract_nums(*num):
    """Subtract numbers in sequence.

    The first number is taken as the starting point, 
    and all following numbers are subtracted from it.

    :param int num: One or more numbers to subtract.
    :returns: The result of sequential subtraction.
    :rtype: int

    Example::
        >>> subtract_nums(100, 20, 30, 40)
        10
    """
    sub = num[0]
    for n in num[1:]:
        sub = sub - n
    return sub
