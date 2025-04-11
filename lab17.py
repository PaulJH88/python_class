list_of_animals = []

while True:
    list_of_animals.append(input("Please provide an animal name:\n"))

    end_loop = input("Do you want to continue? Y/N:\n")
    if end_loop == "N":
        break

order = input("Do you want to sort your animal list in ascending(A) or descending(D) order? Please type A or D:\n")

if order == "D":
    sorted_animals = sorted(list_of_animals, reverse=True)
else:
    sorted_animals = sorted(list_of_animals)

print(sorted_animals)
