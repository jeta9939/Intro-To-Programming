# #9.1 ====================================================================

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init___(Self, name, cuisine, number_served, flavors):
        """Initialize attributes"""
        Self.name = name
        Self.cuisine = cuisine
        Self.number_served = 0
        Self.flavors = flavors

    def describeRestaurant(self):
        """describe restaurant name and cuisine"""
        print(f"We want to go to {self.name}")
        print(f"They serve {self.cuisine} food")

    def openRestaurant(self):
        """describe Restaurant opening"""
        print(f"{self.name} is open")

    def countPatrons(self):
        """count customers served"""
        print(f"They've served {self.number_served} customers")

    def increment_number_served(self, customers):
        """incrementally add customers served"""
        self.increment_number_served += customers

# #9.1 - 9.4 ====================================================================
# # (Was having a glitch and I couldn't do the method of listing attributes that is shorter wanted to let you know, would love to know why)

r1 = Restaurant()
r1.name = "Fazollis"
r1.cuisine = "Italian"
r1.number_served = "3"

print(r1.name)
print(r1.cuisine)
print(r1.number_served)
print(r1.number_served)

r1.describeRestaurant()
r1.openRestaurant()
r1.countPatrons()

r2 = Restaurant()
r2.name = "Patties"
r2.cuisine = "Irish"

r3 = Restaurant()
r3.name = "Marias"
r3.cuisine = "Mexican"
   
print(r2.name)
print(r2.cuisine)

print(r3.name)
print(r3.cuisine)

r2.describeRestaurant()
r2.openRestaurant()    

r3.describeRestaurant()
r3.openRestaurant() 

#9.6 IceCream ====================================================================


class IceCreamStand(Restaurant):
    """Represents restaurant of IceCreamStand variety"""

    def __init__(self, name, cuisine, flavors):
        """initialize attributes of parent class"""
        super().__init__(name, cuisine, flavors)

    def listFlavors(self):
        """list flavors of icecream"""
        print(f"We have: {self.flavors}")

r4 = IceCreamStand
r4.name = "Swirlies"
r4.cuisine = "Ice Cream"
r4.flavors = "vanilla, strawberry, chocolate, caramel, mint, and cookie dough."

r4.describeRestaurant
r4.listFlavors