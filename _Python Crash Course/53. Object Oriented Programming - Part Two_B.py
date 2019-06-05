# Base class
class Animal():

    def __init__(self,fur):
        # print('Animal Created!')
        self.fur = fur

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating!')

# Derived class
# Inheriting Animal attributes and methods
class Dog(Animal):

    def __init__(self,fur):
        Animal.__init__(self,fur)
        print('Dog Created!')

    # Overwriting a method
    def report(self):
        print('I am a dog!')

# # ANIMAL
# a = Animal()
# a.eat()
# a.report()

# DOG
d = Dog('Fuzzy')
d.eat()
d.report()
print(d.fur)
