class Pizza():

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

class Topping():

    def __init__(self, name, num_pieces):
        self.name = name
        self.num_pieces = num_pieces

    def __repr__(self):
        return "{} pieces of {}".format(self.num_pieces, self.name)

pizza = Pizza()
pizza.add_topping(Topping("pepperoni", 18))
pizza.add_topping(Topping("mushrooms", 12))
pizza.add_topping(Topping("green peppers", 15))
print(pizza.toppings)