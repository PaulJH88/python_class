person = {
    "f_name": "Mariya",
    "l_name": "Nalla",
    "age": 33,
}

print(person)
person["Address"] = "Stockholmes"
print(person)

print(person["age"])
print(person["f_name"])
print(person.get("l_name"))

print(person.keys())
print(person.values())
print(person.items())

for x in person.items():        #person.keys(), perosn.values()
    print(x)