fruits = []
match = False

while match == False:
    input_fruit = input("Please provide a fruit ")
    if input_fruit in fruits:
        match = True
        print(fruits)
    else:
        fruits.append(input_fruit)
    
