from basic import db, Puppy

db.create_all()

sam = Puppy('Sam', 3)
frank = Puppy('Frank', 4)

print(sam.id)
print(frank.id)

# db.session.add(sam)
# db.session.add(frank)
# or
db.session.add_all([sam, frank])

db.session.commit()

print(sam.id)
print(frank.id)