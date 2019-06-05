from models import db, Puppy, Owner, Toy

# rufus = Puppy('Rufus')
# db.session.add(rufus)
# db.session.commit()
print(Puppy.query.all())

# mike = Owner('Mike', rufus.id)
# db.session.add(mike)
# db.session.commit()
print(Owner.query.all())

print(Puppy.query.filter_by(name='Rufus').all())
print(Owner.query.filter_by(name='Mike').all())