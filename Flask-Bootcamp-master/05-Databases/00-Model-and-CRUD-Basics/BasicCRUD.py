# Now that the table has been created by running
# BasicModelApp and SetUpDatabase we can play around with CRUD commands
# This is just an overview, usually we won't run a single script like this
# Our goal here is to just familiarize ourselves with CRUD commands

from BasicModelApp import db,Puppy

###########################
###### CREATE ############
#########################
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

###########################
###### READ ##############
#########################
# Note lots of ORM filter options here.
# filter(), filter_by(), limit(), order_by(), group_by()
# Also lots of executor options
# all(), first(), get(), count(), paginate()

all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
print('\n')
# Grab by id
puppy_one = Puppy.query.get(1)
print(puppy_one)
print(puppy_one.age)
print('\n')
# Filters
puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
print(puppy_sam)
print('\n')
###########################
###### UPDATE ############
#########################

# Grab your data, then modify it, then save the changes.
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()


###########################
###### DELETE ############
#########################
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


# Check for changes:
all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
