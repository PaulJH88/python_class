fav_movies = ["Braveheart", "LotR", "Boondock Saints", "Gladiator", "Terminator 2"]
hobbies = ["Soccer", "Gaming", "Movies", "D&D"]
numbers = [11, 15, 5, 7]
ice_cream_flavors = ["Caramel Cone", "Peanut Butter Cup", "Snickers", "Cookie Dough"]

sorted_num = sorted(numbers, reverse=True)
print(sorted_num)

print(hobbies)
hobbies.remove("D&D")
print(hobbies)

print(ice_cream_flavors)
ice_cream_flavors.append("Butterfinger")
print(ice_cream_flavors)

ice_cream_flavors.clear()
print(ice_cream_flavors)

print("Total number of list items:", len(fav_movies) + len(hobbies) + len(numbers) + len(ice_cream_flavors))