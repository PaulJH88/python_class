# def ex1():

#     num1 = 100
#     print(num1, id(num1))

#     num2 = 100
#     print(num2, id(num2))

# def ex2():

#     num3 = 200
#     print(num3, id(num3))

#     num1 = "USA"
#     num4 = num1
#     print(num4, id(num4))
#     print(num1, id(num1))

# num5 = 100
# print(num5, id(num5))

# print(globals())

# if __name__ == "__main__":
#     ex1()
   
# ex2()

import math


def main():
    print("What is side a? ")
    a = float(input())
    print("What is side b? ")
    b = float(input())
    c = hypotenuse(a, b)
    
    print(c)

def hypotenuse(a, b):
    return math.sqrt(a*a + b * b)

if __name__ == "__main__":

    main()

