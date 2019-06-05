from basic import db, Puppy

# CREATES ALL THE TABLES Model --> Db Table
# Transforms your Model class to a database table
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

print(sam.id) # Prints NONE
print(frank.id) # Prints NONE

# Add both together
db.session.add_all([sam, frank])

'''
or add it individually
db.session.add(sam)
db.session.add(frank)
'''

db.session.commit()

print(sam.id) 
print(frank.id)