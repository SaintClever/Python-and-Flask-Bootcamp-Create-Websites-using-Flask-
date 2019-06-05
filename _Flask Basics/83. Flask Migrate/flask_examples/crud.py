from basic import db, Puppy


''' CREATE '''
rufus = Puppy('Rufus', 5)
# db.session.add(rufus)
# db.session.commit()


''' READ '''
filter_rufus = Puppy.query.filter_by(name='Rufus')
# print(filter_rufus.all())

# get_third_pup = Puppy.query.get(3)
# print(get_third_pup)


''' UPDATE '''
# get_third_pup.name = 'Spot'
# get_third_pup.age = '6'
# db.session.commit()


''' DELETE '''
# db.session.delete(get_third_pup)
# db.session.commit()

puppies = Puppy.query.all()
print(puppies)