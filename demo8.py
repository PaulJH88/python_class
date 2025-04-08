class Dish:
    def __init__(self, name, country, ingredients, desc):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.desc = desc

    def display(self):
        print("\n\nName of the Dish is: ", self.name)
        print("Country of origin: ", self.country)
        print("List of ingredients: ", self.ingredients)
        print("Description: ", self.desc)

d1 = Dish("Pizza", "Italy", ["Dough", "Tomatoes", "Capsicum", "Mushroom", "Jelepenos", "Olives"], 
          "we make a base and spread all the toppings on the base and bake it")
d1.display()

d2 = Dish("Dal", "India", ["Lentils", "Spices", "Salt", "Peanuts", "oil"], 
          "Cook lentils and add spices to it, add some water and add oil and tadka")
d2.display()

d1.ingredients.append("Onions")
d1.display()