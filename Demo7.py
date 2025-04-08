colors = ["Blue", "Red", "Black", "Green", "White"]
pizza = ["Farmhouse", "Extravagenza", "Cheesy", "Mushroom"]
city = ["New York", "Chicago", "Sacramanto", "New Jersy"]
lists = [colors, pizza, city]

print(lists)

for x in lists:
    for y in x:
        if y == "Chicago":
            break
        print("Element: ", y)
    else:
        print("Done!")