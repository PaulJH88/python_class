names = {"Bob", "Jane", "Tom", "Gandolf"}
numbers = {1,2,3,5,8,13,21,34}
names_and_numbers = names.union(numbers)

print(names)
print(numbers)
print(names_and_numbers)
    
print(names.issubset(names_and_numbers))
print(names_and_numbers.issuperset(numbers))

numbers.remove(3)
names.add("Tim")

numbers_and_combined = numbers.union(names_and_numbers)

differences = names.difference(numbers)
print(differences)
