def add_subtract(x, y, operation):
    
    def add_things(x, y):
        return (x+y)
        
    def subtract_things(x,y):
        return (x-y)
    
    if operation == "+":
        return add_things(x,y)
    elif operation == "-":
        return subtract_things(x,y)
    else:
        raise Exception("Please enter '+' to add, or '-' to subtract")
    

def mult_div(x, y, operation):

    def mult_things(x, y):
        return (x*y)
        
    def div_things(x, y):
        return (x/y)
    
    if operation == "*":
        return mult_things(x,y)
    elif operation == "/":
        return div_things(x,y)
    else:
        raise Exception("Please enter '*' to multiply, or '/' to divide")
    
x = 5
y = 4

print(add_subtract(x,y,"+"))
print(add_subtract(x,y,"-"))

print(mult_div(x,y,"*"))
print(mult_div(x,y,"/"))

