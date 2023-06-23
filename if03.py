def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
   
    """
    mx = max(a,b,c)
    mn = min(a,b,c)
    if mx==a and mn==c:
        return b
    if mx==b and mn==c:
        return a
    if mx==c and mn==a:
        return b
    if mx==b and mn==a:
        return c
        
        
a,b,c = 12,15,87
print(main(a,b,c))
a,b,c=345,876,954
print(main(a,b,c))