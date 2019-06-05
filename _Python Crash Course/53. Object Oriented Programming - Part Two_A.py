class Circle():

    # Class object attribute because 3.14 is absolute
    pi = 3.14

    def __init__(self,radius=1): # default value
        self.radius = radius

    # Method for calculating area
    def area(self):
        return self.radius * self.radius * self.pi

    # Method for calculating circumfrence
    def circumfrence(self):
        return 2 * self.pi * self.radius


mycircle = Circle()
print(mycircle.radius)

# or
mycircle = Circle(10)
print(mycircle.radius)
print(mycircle.area()) # call methods by instance.method_name()
print(mycircle.circumfrence())
