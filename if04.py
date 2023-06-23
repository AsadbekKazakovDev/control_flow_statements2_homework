def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        return 0
    if a!=b:
        return max(a,b)
a,b = 43,23
print(main(a,b))
a,b = -7,87
print(main(a,b))
a,b = 4,4
print(main(a,b))