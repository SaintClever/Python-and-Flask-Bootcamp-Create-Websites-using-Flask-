
################################################################################
####################-----------------------------###############################
####################-----------LOOPS-------------###############################
####################-----------------------------###############################
################################################################################

# Time to review loops with Python, such as For Loops and While loops
# Python is unique in that is discards parenthesis and brackets in favor of a
# whitespace system that defines blocks of code through indentation, this forces
# the user to write readable code, which is great for future you looking back at
# your older code later on!

#####################
### FOR LOOPS #######
#####################

# Use For Loops for any sequence of elements. If you try to use a for loop with
# a mapping like a dictionary, it will still work, but it won't loop with any
# order. Let's walk through some examples of how a for loop behaves with the
# various data structures we've learned about!

## For Loop with a list

# Perform an action with each element
seq = [1,2,3,4,5]

for item in seq:
    print(item)


# Perform an action for every element but doesn't actually involve the elements
for item in seq:
    print('Yep')


# You can call the loop variable whatever you want:
for jelly in seq:
    print(jelly+jelly)

## For Loop with a Dictionary
ages = {"Sam":3,"Frank":4,"Dan":29}

for key in ages:
    print("This is the key")
    print(key)
    print("This is the value")
    print(ages[key])
    print("\n")

# A list of tuple pairs is a very common format for functions to return data in
# Because it is so common we can use tuple un-packing to deal with this, example:

mypairs = [(1,10),(3,30),(5,50)]

# Normal
for tup in mypairs:
    print(tup)

# Tuple un-packing
for item1,item2 in mypairs:
    print(item1)
    print(item2)

#######################
### WHILE LOOPS #######
#######################

# While loops allow us to continually perform and action until a condition
# becomes true. For example:

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

#####################
### OTHER TOPICS ####
#####################

# RANGE FUNCTION
# range() can quickly generate integers for you, based on a starting and ending point

# Note that its a generator:
range(5)

list(range(5))

for i in range(5):
    print(i)

# Start and ending
range(1,10)

# Third argument for step-size
range(0,10,2)
