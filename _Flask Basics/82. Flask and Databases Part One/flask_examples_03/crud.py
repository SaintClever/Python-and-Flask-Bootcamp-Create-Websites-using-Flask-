from basic import db, Puppy

puppies = Puppy.query.all()
# print(puppies)


''' CREATE '''
# rufus = Puppy('Rufus', 5)
# db.session.add(rufus)
# db.session.commit()
# print(puppies)


''' READ '''
# filter_rufus = Puppy.query.filter_by(name='Rufus')
# print(filter_rufus.all())


''' UPDATE '''
# get_rufus = Puppy.query.get(3)
# print(get_rufus)
# print(get_rufus.name)
# print('')

# get_rufus.name = 'Spot'
# get_rufus.age = 6
# db.session.add(get_rufus)
# db.session.commit()
# print(get_rufus)

# print(puppies)


''' DELETE '''
# delete_spot = Puppy.query.get(3)
# print(delete_spot)
# print('')

# db.session.delete(delete_spot)
# db.session.commit()

print(puppies)