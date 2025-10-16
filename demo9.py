name = "Bob"
print(name)
l1 = [1,2,3,4,5]

try:
    # del name
    print(name)

    print(l1[7])
except IndexError as ie:
    pass
    # print("Index Error:", ie)
except Exception as e:                  #Exception is the parent class of all the exceptions, so it has to be at the end
    print("Error: ", e)

# raise IndentationError

print("Maximum:",min(l1))           #Logical error