def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    m=a
    if m>b:
        m=b
    if m>c:
        m=c
    return m
a,b,c = 470,60,89
print(main(a,b,c))
a,b,c = -87,-45,97
print(main(a,b,c))