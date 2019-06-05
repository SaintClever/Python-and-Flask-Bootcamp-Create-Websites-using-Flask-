from basic import db, Puppy

db.create_all()

sam = Puppy('Sam', 3)
frank = Puppy('Frank', 4)

db.session.add_all([sam,frank])
db.session.commit()

puppies = Puppy.query.all()
print(puppies)