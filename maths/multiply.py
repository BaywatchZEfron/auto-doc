def multiply_nums(*num):
    """Multiply numbers together.

    :param int num: One or more numbers to multiply.
    :returns: The product of all numbers provided.
    :rtype: int

    Example::
        >>> multiply_nums(2, 3, 4)
        24
    """
    mult = 1
    for n in num:
        mult = mult * n
    return mult
