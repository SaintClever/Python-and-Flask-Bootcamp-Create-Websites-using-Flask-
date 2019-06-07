#BAIC.PY
# CREATE ENTRIES INTO THE TABLES!
from models import db, Puppy, Owner, Toy

''' CREATE ''' # puppy
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DB
db.session.add_all([rufus,fido])
db.session.commit()

# print db
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first() #.first() vs .all()
print(rufus)

''' CREATE ''' # owner
# CREATE OWNER OBJECT
jose = Owner('Jose', rufus.id)


''' CREATE ''' # toys
# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose,toy1,toy2])
db.session.commit()

# GRAB RUFUS AFTER THOSE ADDITIONS!
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)


rufus.report_toys()