def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    b = n//10000
    c = (n//1000)%10
    d = (n//100)%10
    e = (n//10)%10
    f = n%10
    return max(b,c,d,e,f)
n = 12345
print(main(n))
n = 98765
print(main(n))