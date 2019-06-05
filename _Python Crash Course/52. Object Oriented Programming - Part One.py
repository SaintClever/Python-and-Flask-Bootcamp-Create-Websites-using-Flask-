# mylist = [1,2,3]
#
# mylist.append(4)
#
# print(type(mylist))
# print(type(12))
# print(type(23.5))

# class Sample(): # class names use camleCase not under_score
#     pass
#
# x = Sample()
# print(type(x))

class Dog():

    # CLASS OBJECT ATTRIBUTES - An attribute thats perminitely set and is always true
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Huskie','Sammy')
new_dog = Dog('Golden','Cindy')

# print(type(sam))
# print(type(sam.breed))

print(sam.breed)
print(sam.name)
print(sam.species)
print('')

# print(new_dog)
print(new_dog.species)
