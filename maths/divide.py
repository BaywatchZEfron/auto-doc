def divide_nums(*num):
    """Divide numbers in sequence.

    The first number is taken as the starting point,
    and all following numbers divide the current result.
    hakuna matata

    :param int num: Two or more numbers to divide.
    :returns: The result of sequential division.
    :rtype: float

    Example::
        >>> divide_nums(100, 2, 5)
        10.0
    """
    div = num[0]
    for n in num[1:]:
        div = div / n
    return div
