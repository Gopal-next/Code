def smallest_even_multiple(n: int) -> int:
    """
    Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

    :param n: A positive integer
    :return: The smallest positive integer that is a multiple of both 2 and n
    """
    if n % 2 == 0:
        return n
    else:
        return n * 2
    
print(smallest_even_multiple(5))  # Output: 10
print(smallest_even_multiple(6))  # Output: 6
print(smallest_even_multiple(1))  # Output: 2