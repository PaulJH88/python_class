#Numeric
#integers
num1 = 100
print(num1, id(num1), type(num1))

#float
num2 = 100.12
print(num2, id(num2), type(num2))

#complex
num3 = 10 + 15j
print(num3, id(num3), type(num3))

#string
str1 = 'First'
str2 = "Last"
str3 = """
    Lives in 

"""

str4 = '''

       City
'''
print(str1+str2)
print(str1+str3+str4)
print(str1, id(str1), type(str1))

#boolean
val = True
print(val, id(val), type(val))

Val2Do = 10             #Valid
Val = 10                #Valid
val = 10                #Valid
vVal = 10               #Valid
#12 = 10                 #InValid
#1Val = 200              #InValid
#val@123 = 300           #InValid
print(val@123)          
val_123 = 123           #Valid
#Val-123 = 123           #InValid

_val = 100              #Valid #prefix with underscore makes it private

#try = 100               #inValid    cannot have keywords as variable names

str1 = "15.25"
print(str1, id(str1), type(str1))

num1 = float(str1)
print(num1, id(num1), type(num1))

num10 = int(num1)
print(num10, id(num10), type(num10))

str2 = "Himadrie"       
#n2 = int(str2)          #invalid type conversion