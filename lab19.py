def print_ingredients(ingredients_list):
    for ingredient in ingredients_list.items():
        print(ingredient)
    print("\n")

def recipe_desc(desc, category="N/A"):
    print("Description:", desc)
        
    print("Category:", category)


#recipe for mac and cheese
mac_ingredients = {
    "noodles" : "one box",
    "milk" : "1/4 cup",
    "butter" : "1/4 cup",
    "cheese sauce" : "1 packet"
}

grilled_cheese_ingredients = {
    "bread" : "two slices",
    "cheese" : "two slices",
    "butter" : "light coverage"
}

print_ingredients(mac_ingredients)
print_ingredients(grilled_cheese_ingredients)

recipe_desc("Noodles covered in cheese sauce")
recipe_desc("Noodles covered in cheese sauce", "Quick meal")
recipe_desc(desc = "Buttered bread, with cheese in the middle, grilled until bread is golden brown, and cheese is melted.", category="Kids love it!")