def add_or_subtract(x, y, operation):
    def add(nr1, nr2):
        return nr1 + nr2

    def subtract(nr1, nr2):
        return nr1 - nr2

    if operation == "Add":
        return add(x, y)
    elif operation == "subtract":
        return subtract(x, y)

def multiply_or_divide(x, y, operation):
    def multiply(nr1, nr2):
        return nr1 * nr2

    def divide(nr1, nr2):
        return nr1 / nr2

    if operation == "multiply":
        return multiply(x, y)
    elif operation == "divide":
        return divide(x, y)

print(add_or_subtract(20,10,"Add"))
print(add_or_subtract(20,10,"subtract"))
print(multiply_or_divide(20,10,"multiply"))
print(multiply_or_divide(20,10,"divide"))

X =1000                                 #global variable

def ext(num1, num2):
    a = 100                             #local variable

    z = X+num1+num2 +a
    print("Addition: ", z)

    def sub():
        b = 200                         #nested variable
        z = X-b-a-num1-num2
        print("Subtraction: ", z)

    sub()

print("X",X)
ext(20, 30)