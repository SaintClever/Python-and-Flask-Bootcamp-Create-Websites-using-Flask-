# This script will create some puppies, owners, and toys!
# Note, if you run this more than once, you'll be creating dogs with the same
# name and duplicate owners. The script will still work, but you'll see some
# warnings. Watch the video for the full explanation.
from models import db,Puppy,Owner,Toy

# Create 2 puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

# Add puppies to database
db.session.add_all([rufus,fido])
db.session.commit()

# Check with a query, this prints out all the puppies!
print(Puppy.query.all())

# Grab Rufus from database
# Grab all puppies with the name "Rufus", returns a list, so index [0]
# Alternative is to use .first() instead of .all()[0]
rufus = Puppy.query.filter_by(name='Rufus').all()[0]

# Create an owner to Rufus
jose = Owner("Jose",rufus.id)

# Give some Toys to Rufus
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy("Ball",rufus.id)

# Commit these changes to the database
db.session.add_all([jose,toy1,toy2])
db.session.commit()

# Let's now grab rufus again after these additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

# Show toys
print(rufus.report_toys())

# You can also delete things from the database:
# find_pup = Puppy.query.get(1)
# db.session.delete(find_pup)
# db.session.commit()
