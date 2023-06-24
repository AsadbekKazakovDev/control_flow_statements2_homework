def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    m=a
    if m<b:
        m=b
    if m<c:
        m=c
    return m
a,b,c = 4,6,8
print(main(a,b,c))