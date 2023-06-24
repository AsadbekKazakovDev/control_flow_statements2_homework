def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    s=""
    if temp<0:
        s="Freezing"
    if temp>0 and temp<11:
        s="Very Cold"
    if temp>10 and temp<21:
        s="Cold"
    if temp>20 and temp<31:
        s="Normal"  
    if temp>30 and temp<41:
        s="Hot"   
    if temp>40:
        s="Very Hot"
    return s
temp = 32
print(main(temp))
temp = 86
print(main(temp))
temp = 12
print(main(temp))
temp = 25
print(main(temp))
temp = -44
print(main(temp))