dog = {
    "name": "Dodgeball",
    "breed": "Mastiff",
    "age": 12
}

print(dog)
dog["owner"] = "Bob"

print(dog)

dog_values = []

for val in dog.values():
    dog_values.append(val)

print(dog_values)

breed = dog["breed"]
print(breed)

dog_copy = dog.copy()

print(dog_copy)

dog.pop("owner")

print(dog)
print(dog_copy)