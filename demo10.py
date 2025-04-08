fruits = ["Grapes", "Apple", "Banana", "Cherries", "Apple","Kiwi", "Watermelon", 
          "Orange", "Peach", "Apple","Mango", "Strawberry"]
print(fruits.count("Apple"))                    #Counts the frequency
print(len(fruits))                              #finds the length of the list
fruits.append("Dragon Fruit")                   #adds the given element at the end
print(fruits)           
fruits.insert(3, "Strawberry")                  #insert element at the given index
print(fruits)       
fruits.remove("Apple")                          #removes the given element
print(fruits)
fruits.pop()                                    #removes the last element from the list
print(fruits)
fruits.pop(5)                                   #removes the element at the given index
print(fruits)

fruits.reverse()                                #reverses the sequence of the list
print(fruits)
fruits.sort()                                   #sort the list in ascending order
print(fruits)
nums = [11,54,88,35]
fruits.extend(nums)                             #adds one list to the other
print(fruits)
print(nums)

fr = fruits.copy()                              #creates a new list by copying the contents
print(fr)
print(fruits)
fruits.clear()                                  #clears the content of the list
print(fruits)