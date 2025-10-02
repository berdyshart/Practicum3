import math
a = int(input())
b = int(input())
c = int(input())
print(math.acos( (b**2 + c**2 - a**2)/(2*b*c) ) / math.pi * 180)
print(math.acos( (a**2 + c**2 - b**2)/(2*a*c) ) / math.pi * 180)
print(math.acos( (b**2 + a**2 - c**2)/(2*b*a) ) / math.pi * 180)