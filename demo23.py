# import math as m
from math import log10, floor, ceil
from math import sqrt as sq
import random

num1 = int(input("Please enter first num: "))
num2 = float(input("Please enter second num: "))

res = random.randint(num1, num2)

print(res)
result = log10(res)
print(result)

print(sq(res))
print(floor(res))
print(ceil(res))