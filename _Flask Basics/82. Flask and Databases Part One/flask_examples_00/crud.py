from basic import db, Puppy


# CREATE
# rufus = Puppy('Rufus', 5)
# db.session.add(rufus)
# db.session.commit()


# READ
all_puppies = Puppy.query.all() # print(all_puppies)

puppy_one = Puppy.query.get(1) # read a specific id
print(puppy_one)

puppy_two = Puppy.query.get(2)
print(puppy_two)

puppy_three = Puppy.query.get(3)
print(puppy_three)


# FILTER
puppy_frank = Puppy.query.filter_by(name='Frank')
print(puppy_frank.all())
print('')

puppy_sam = Puppy.query.filter_by(name='Sam')
print(puppy_sam.all())
print('')

puppy_rufus = Puppy.query.filter_by(name='Rufus')
print(puppy_rufus.all())
print('')


# UPDATE
first_puppy = Puppy.query.get(1)
first_puppy.name = 'Teddy'
first_puppy.age = 100
db.session.add(first_puppy)
db.session.commit()

# second_puppy = Puppy.query.get(2)
# second_puppy.name = 'Kate'
# second_puppy.age = 25
# db.session.add(second_puppy)
# db.session.commit()

# third_puppy = Puppy.query.get(3)
# third_puppy.age = 300
# third_puppy.name = 'Bill'
# db.session.add(third_puppy)
# db.session.commit()


# DELETE
# second_pup = Puppy.query.get(2)
# db.session.delete(second_pup)
# db.session.commit()

# third_pup = Puppy.query.get(3)
# db.session.delete(third_pup)
# db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)