def main(n):
    """
    Find the index of the largest digit of the five-digit number.
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
    mx = max(b,c,d,e,f)
    md = 0
    if mx==b:
        md+=1
    if mx==c:
        md+=2
    if mx==d:
        md+=3
    if mx==e:
        md+=4
    if mx==f:
        md+=5
    return md
n = 12348
print(main(n))
n=32897
print(main(n))
n=46935
print(main(n))
