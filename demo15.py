s1 = {11,33,44,22,66,77,99,55,88,11,44,77,22,11}
s2 = {11,77,44}
s3 = {"Python", "C#", "Java", "Scala"}
print(s1)                   #allows only unique values

s1.add("Python")            #positions are random, we cannot access using index
print(s1)

s1.remove(11)
print(s1)

s1.pop()
print(s1)

s1.add("C#")
print(s1)

print(s1.union(s3))         #combines two sets
print(s1.difference(s3))    #removes common elements from the first set

print(s1.intersection(s3))  #displays only common elements
    
print(s3.isdisjoint(s2))    #if two sets have anything in common or not